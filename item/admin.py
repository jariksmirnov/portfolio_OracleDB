from django.contrib import admin

from .models import BusinessArea, Company, Item

admin.site.register(BusinessArea)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
                    'company_id',
                    'company_name',
                    'director',
                    'business_area',
                    'is_active',
                    'created_by',
                    #  'turnover_per_year',
                    'tax'
                    #  'taxes',
                    )


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
                    'product_id',
                    'product_name',
                    'price',
                    'in_market',
                    'created_by',
                    )
