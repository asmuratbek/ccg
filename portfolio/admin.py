from django.contrib import admin
from .models import *


# Register your models here.

class PortfolioElementsInlines(admin.StackedInline):
    model = PortfolioElements


class PortfolioAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)
    list_display = ('title', 'created_at',)
    inlines = [PortfolioElementsInlines]


admin.site.register(Category)
admin.site.register(Portfolio, PortfolioAdmin)
