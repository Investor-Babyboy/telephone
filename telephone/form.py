from django.forms import ModelForm
from .models import Telephone

class TelephoneForm(ModelForm):
    class Meta:
        model = Telephone
        exclude = ['date_created', 'date_updated']