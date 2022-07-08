from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Pessoas
from .forms import PessoasForm

class ListaPessoasView(ListView):
    model = Pessoas
    queryset = Pessoas.objects.all().order_by('nome_completo')

class PessoasCreateView(CreateView):
    model = Pessoas
    form_class = PessoasForm
    success_url = '/pessoas/'

class PessoasUpdateView(UpdateView):
    model = Pessoas
    form_class = PessoasForm
    success_url = '/pessoas/'
