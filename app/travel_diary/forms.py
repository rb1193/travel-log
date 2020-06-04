from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from .models import Diary

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['name', 'cover_image']