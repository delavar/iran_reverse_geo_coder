from django.contrib import admin

from location.models import Province, County, City


class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Province, ProvinceAdmin)


class CountyAdmin(admin.ModelAdmin):
    list_display = ('name', 'province')


admin.site.register(County, CountyAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'province', 'county')


admin.site.register(City, CityAdmin)
