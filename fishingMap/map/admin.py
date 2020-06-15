from django.contrib import admin
from import_export import resources, fields
from import_export.widgets import ManyToManyWidget, ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
from .models import city, area, monthChoices, branches, fingerling, fishingStatus

#register models to django admin

#admin.site.register(area)
#admin.site.register(monthChoices)
#admin.site.register(fishingStatus)
#admin.site.register(city)
#admin.site.register(branches)
#admin.site.register(fingerling)


@admin.register(area)
class areaAdmin(ImportExportModelAdmin):
    city = fields.Field(widget = ForeignKeyWidget(city, 'city'))
    class Meta:
        #fields = ('location', 'lat', 'lon', 'city', 'district')
        model = area
    #list_display = ('location', 'lat', 'lon', 'city', 'district')

@admin.register(monthChoices)
class monthChoicesAdmin(ImportExportModelAdmin):
    list_display = ('month',)

@admin.register(fishingStatus)
class fishingStatusAdmin(ImportExportModelAdmin):
    list_display = ('fish', 'area', 'time')

@admin.register(city)
class cityAdmin(ImportExportModelAdmin):
    list_display = ('city',)

@admin.register(branches)
class branchesAdmin(ImportExportModelAdmin):
    city = fields.Field(attribute = 'city', widget = ManyToManyWidget(city, 'city'))
    month = fields.Field(attribute = 'month', widget = ManyToManyWidget(monthChoices, 'month'))
    class Meta:
        model = branches
    #list_display = ('name', 'city', 'month')

@admin.register(fingerling)
class fingerlingAdmin(ImportExportModelAdmin):
    list_display = ('name', 'nickname', 'branch')
