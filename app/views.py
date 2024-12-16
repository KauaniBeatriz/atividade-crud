from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import Funcionario
from .forms import FuncionarioForm  # Formulário que cria/edita o funcionário

class FuncionarioView(View):
    def get(self, request, pk=None):
        if pk:  # Se houver um ID, significa que estamos editando ou excluindo
            funcionario = get_object_or_404(Funcionario, pk=pk)
            form = FuncionarioForm(instance=funcionario)
            return render(request, 'form_funcionario.html', {'form': form, 'funcionario': funcionario, 'action': 'editar'})
        else:  # Se não houver ID, significa que estamos criando um novo funcionário
            form = FuncionarioForm()
            return render(request, 'form_funcionario.html', {'form': form, 'action': 'criar'})

    def post(self, request, pk=None):
        if pk:  # Se houver um ID, significa que estamos editando ou excluindo
            funcionario = get_object_or_404(Funcionario, pk=pk)
            if 'deletar' in request.POST:  # Se o botão "Deletar" foi pressionado
                funcionario.delete()
                return redirect('listar_funcionarios')
            else:  # Se o formulário de edição for enviado
                form = FuncionarioForm(request.POST, instance=funcionario)
                if form.is_valid():
                    form.save()
                    return redirect('listar_funcionarios')
        else:  # Se não houver ID, estamos criando um novo funcionário
            form = FuncionarioForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('listar_funcionarios')
        return render(request, 'form_funcionario.html', {'form': form})

from django.views.generic import ListView
from .models import Funcionario

class FuncionarioListView(ListView):
    model = Funcionario
    template_name = 'listar_funcionarios.html'  # Certifique-se de ter esse template
    context_object_name = 'funcionarios'  # Nome da variável no template

def post(self, request, pk=None):
    if pk:
        funcionario = get_object_or_404(Funcionario, pk=pk)
        if 'deletar' in request.POST:
            funcionario.delete()  # Excluir o funcionário
            return redirect('listar_funcionarios')
        else:
            form = FuncionarioForm(request.POST, instance=funcionario)
            if form.is_valid():
                form.save()
                return redirect('listar_funcionarios')
    else:
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_funcionarios')
    return render(request, 'form_funcionario.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Funcionario

def exibir_funcionario(request, pk):
    # Obtém o funcionário pelo PK (id)
    funcionario = get_object_or_404(Funcionario, pk=pk)

    # Renderiza o template com os dados do funcionário
    return render(request, 'exibir_funcionario.html', {'funcionario': funcionario})


