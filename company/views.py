from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewCompanyForm, EditCompanyForm
from item.models import BusinessArea, Company


def companies(request):
    query = request.GET.get('query', '')
    business_area_id = request.GET.get('business_area', 0)
    business_areas = BusinessArea.objects.all()
    companies = Company.objects.filter(is_active=True)

    if business_area_id:
        companies = companies.filter(business_area_id=business_area_id)

    if query:
        companies = companies.filter(Q(company_name__icontains=query) | Q(director__icontains=query))

    return render(request, 'company/companies.html', {
        'companies': companies,
        'query': query,
        'business_areas': business_areas,
        'business_area_id': int(business_area_id),
    })


def detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    related_companies = Company.objects.filter(business_area=company.business_area, is_active=True).exclude(pk=pk)[0:4]

    return render(request, 'company/detail.html', {
        'company': company,
        'related_companies': related_companies
    })


def detail_taxes(request, pk):
    company = get_object_or_404(Company, pk=pk)
    related_companies = Company.objects.filter(business_area=company.business_area, is_active=True).exclude(pk=pk)[0:4]

    return render(request, 'company/detail_taxes.html', {
        'company': company,
        'related_companies': related_companies
    })


@login_required()
def new(request):
    if request.method == 'POST':
        form = NewCompanyForm(request.POST, request.FILES)

        if form.is_valid():
            company = form.save(commit=False)
            company.created_by = request.user
            company.save()

            return redirect('company:companies', pk=company.id)
    else:
        form = NewCompanyForm()

    return render(request, 'company/form.html', {
        'form': form,
        'title': 'New Company',
    })


@login_required
def delete(request, pk):
    company = get_object_or_404(Company, pk=pk, created_by=request.user)
    company.delete()

    return redirect('company:companies')


@login_required()
def edit(request, pk):
    company = get_object_or_404(Company, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditCompanyForm(request.POST, request.FILES, instance=company)

        if form.is_valid():
            form.save()

            return redirect('company:detail', pk=company.id)
    else:
        form = EditCompanyForm(instance=company)

    return render(request, 'company/form.html', {
        'form': form,
        'title': 'Edit Company',
    })
