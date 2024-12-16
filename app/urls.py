from django.urls import path
from .views import FuncionarioListView, FuncionarioView, exibir_funcionario  # Certifique-se de importar a função exibir_funcionario

urlpatterns = [
    path('form_funcionario/', FuncionarioView.as_view(), name='form_funcionario'),
    path('form_funcionario/<int:pk>/', FuncionarioView.as_view(), name='form_funcionario'),
    path('listar_funcionarios/', FuncionarioListView.as_view(), name='listar_funcionarios'),
    path('exibir_funcionario/<int:pk>/', exibir_funcionario, name='exibir_funcionario'),  # Defina a URL para a exibição de dados
]


