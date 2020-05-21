from django.contrib import admin
from .models import city, area, monthChoices, branches, fingerling


admin.site.register(area)
admin.site.register(monthChoices)

admin.site.register(city)
admin.site.register(branches)
admin.site.register(fingerling)