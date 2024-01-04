from django import forms
from .models import Person


class personform(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
