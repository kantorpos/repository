from django import forms
from .models import Repo

class RepoModelForm(forms.ModelForm):
    class Meta:
        model = Repo
        widgets = {
            'file': forms.FileInput(attrs={'accept': '.pdf'}),
        }
        fields = (
            'file',
            'title',
        )
        
class RepoModelUpdateForm(forms.ModelForm):
    class Meta:
        model = Repo
        fields = (
            'title',
            'status',
        )