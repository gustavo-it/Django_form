from multiprocessing import context
from django.shortcuts import render
from .forms import ContatoForm, ProdutoModelForm  # importando os formulários
from django.contrib import messages
from .models import Produto
# Fazendo o import de nosso model Produto


def index(request):
    context = {
        "produtos": Produto.objects.all()
    }
    return render(request, "index.html", context)


def contato(request):
    form = ContatoForm(request.POST or None)
    if str(request.method) == "POST":
        if form.is_valid():
            form.send_mail()
            messages.success(request, "E-mail enviado com sucesso!")
            # Essa mensagem irá aparecer em nossa página web
            form = ContatoForm()
        else:
            messages.error(request, "erro ao enviar e-mail")
    form = ContatoForm()
    context = {"form": form}
    return render(request, "contato.html", context)


def produto(request):
    """
    Se o request.método for igual a POST o formulario vai ser o ProdutoModelForm, passando a requisição
    que é post e o arquivo que serão nossas imagens.
    """
    if str(request.method) == "POST":
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, "Produto salvo com sucesso")
            form.save()
        else:
            messages.error(request, "Erro ao salvar produto")

    form = (
        ProdutoModelForm()
    )  # Caso a requisição não seja post, tudo que está a cima será ignorado
    # Para que a página seja renderizada com o nosso form.

    context = {"form": form}
    return render(request, "produto.html", context)
