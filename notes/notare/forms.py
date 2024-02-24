from django import forms
from .models import Notes

class NoteModelForm(forms.ModelForm):

    class Meta:
        model = Notes
        fields = {
            'title',
            'content',
            'created_at'
        }
