from .models import wimag
from django.forms import ModelForm
class IForm(ModelForm):
    class Meta:
        model=wimag
        fields = ('Hex','cover')