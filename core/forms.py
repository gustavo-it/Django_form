from django import forms

# importando do django a função forms
from .models import Produto

# primeiro vamos importar nosso models, no caso o Produto que criamos anteriomente
from django.core.mail.message import EmailMessage
# Importando EmailMessage para fazer o envio dos emails


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())


    def send_mail(self):
        nome = self.cleaned_data['nome']  # Pegando o valor pela chave e acrescentando em uma variável
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='E-mail enviado pelo nosso sistema de formulário django',  # Assunto do email
            body=conteudo,  # O conteudo do email será os dados que foram enviados através do formulário
            from_email='contato@seudominio.com.br',  # Por quem está sendo enviado o email
            to=['contato@seudominio.com.br',],  # Para quem o email vai ser enviado, note que ele é uma lista
            headers={'Reply-to': email}  # Cabeçalho, ou seja, se alguém for responder esse email, para quem irá responder (para email do usuario)
        )

        mail.send()  # Pega as configurações e dispara o e-mail

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        """
        Note que anteriormente criamos um formulário chamando também de Form que esta herdando de Form.
        Agora estamos criando o nosso Produto chamando também de ModelForm que está herdando de
        ModelForm, isto significa que ambos tem o comportamento diferente, estão herdando de classes diferentes
        """

        model = Produto
        fields = ("nome", "preco", "estoque", "imagem")
        """
        Tenho uma class Meta, onde estou passando meta dados dessa classe, ou seja,
        estou falando pra ela que o model dessa classe é produto, e quero apresentar os campos
        nome, preco, estoque e imagem para que o usuário informe esses campos
        """
