from django import forms
from .models import fishingStatus

class fishingStatusForm(forms.ModelForm):

    class Meta:
        model = fishingStatus
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['time'].widget.attrs.update({'id': 'id_pub_date'})
