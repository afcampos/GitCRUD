from re import L
from django.urls import path
from .views import ListaPessoasView, PessoasCreateView, PessoasUpdateView

urlpatterns = [
    path('', ListaPessoasView.as_view(), name = 'pessoas.index'),
    path('novo/', PessoasCreateView.as_view(), name = 'pessoas.novo'),
    path('editar/<int:pk>', PessoasUpdateView.as_view(), name = 'pessoas.editar')

]