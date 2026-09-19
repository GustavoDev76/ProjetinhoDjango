from django.shortcuts import render


def home_view(request):
    empresa = {'nome_empresa': "Empresa do GS"}
    return render(request,'home.html', empresa)

def perfil_view(request):
    context = {'nome_funcionario': "Gustavo", 'cargo': "Servicos gerais", 'setor': "Repositor"}
    
    return render(request,'produtos.html', context)