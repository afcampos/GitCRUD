from re import L
from django.urls import path
from .views import ListaPessoasView, PessoasCreateView

urlpatterns = [
    path('', ListaPessoasView.as_view(), name = 'pessoas.index'),
    path('novo/', PessoasCreateView.as_view(), name = 'pessoas.novo')
]