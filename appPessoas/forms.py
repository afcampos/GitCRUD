from dataclasses import fields
from django import forms
from .models import Pessoas

class PessoasForm(forms.ModelForm):
    class Meta:
        model = Pessoas
        fields = ['nome_completo','data_nascimento','ativa']

