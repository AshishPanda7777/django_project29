from  django import forms


from app.models import *

class CollegeForm(forms.ModelForm):
    class Meta:
        model=College
        fields='__all__'