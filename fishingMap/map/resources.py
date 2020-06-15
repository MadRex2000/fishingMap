from import_export import resources, fields
from import_export.widgets import ManyToManyWidget
from .models import city, area, monthChoices, branches, fingerling, fishingStatus

"""class areaResource(resources.ModelResource):
    city = fields.Field(
        column_name = 'city',
        attribute = 'city',
        widget = ForeignKeyWidget(city, 'city'))

    class Meta:
        fields = ('location', 'lat', 'lon', 'city', 'district')
        model = area"""

class monthChoicesResource(resources.ModelResource):
    class Meta:
        model = monthChoices

class fishingStatusResource(resources.ModelResource):
    class Meta:
        model = fishingStatus

class cityResource(resources.ModelResource):
    class Meta:
        model = city

class fingerlingResource(resources.ModelResource):
    class Meta:
        model = fingerling

"""class branchesResource(resources.ModelResource):
    city = fields.Field(attribute = 'city', widget = ManyToManyWidget(city))
    month = fields.Field(attribute = 'month', widget = ManyToManyWidget(monthChoices))
    class Meta:
        model = branches"""
