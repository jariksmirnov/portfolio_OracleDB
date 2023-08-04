from django.db import models
from django.contrib.auth.models import User


class BusinessArea(models.Model):
    name = models.CharField(max_length=255)

    objects = models.Manager()

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'BusinessAreas'

    def __str__(self):
        return self.name


class Company(models.Model):
    company_id = models.IntegerField()
    company_name = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    business_area = models.ForeignKey(BusinessArea, related_name='company', on_delete=models.CASCADE)
    turnover_per_year = models.FloatField()
    tax = models.FloatField(default=20)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name='company', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def taxes(self):
        taxes = self.tax * self.turnover_per_year / 100
        return taxes

    objects = models.Manager()

    class Meta:
        ordering = ('company_id',)
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.company_name


class Item(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, related_name='item', on_delete=models.CASCADE, null=True)
    business_area = models.ForeignKey(BusinessArea, related_name='item', on_delete=models.CASCADE)
    price = models.FloatField()
    in_market = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name='item', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    objects = models.Manager()

    class Meta:
        ordering = ('product_id',)
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.product_name
