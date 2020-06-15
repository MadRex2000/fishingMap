from django import forms
from .models import fishingStatus

class fishingStatusForm(forms.ModelForm):

    class Meta:
        model = fishingStatus
        fields = '__all__'
