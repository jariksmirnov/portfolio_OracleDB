from django.shortcuts import render

from item.models import BusinessArea, Company


def index(request):
    companies = Company.objects.filter(is_active=True)
    business_areas = BusinessArea.objects.all()
    return render(request, 'core/index.html', {
        'business_ares': business_areas,
        'companies': companies,
    })


def contact(request):
    return render(request, 'core/contact.html')


def about(request):
    return render(request, 'core/about.html')
