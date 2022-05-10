from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContato

def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request,username=usuario,password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Você fez login com sucesso.')
        return redirect('dashboard')

def logout(request):
    auth.logout(request)
    return redirect('dashboard')

def cadastro(request):
    if request.method != 'POST': # Verifica se não foi enviado um post
        return render(request, 'accounts/cadastro.html')

    nome = request.POST.get('nome') # Obtem o nome do formulario
    sobrenome = request.POST.get('sobrenome') # Obtem o sobrenome do formulario
    email = request.POST.get('email') # Obtem o email do formulario
    usuario = request.POST.get('usuario') # Obtem o usuario do formulario
    senha = request.POST.get('senha') # Obtem a senha do formulario
    senha2 = request.POST.get('senha2') # Obtem a senha2 do formulario

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2: # Valida se algum campo é vazio
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return render(request, 'accounts/cadastro.html')

    try: # Validação de e-mail inválido
        validate_email(email) # Própria do Django
    except:
        messages.error(request, 'E-mail inválido.')
        return render(request, 'accounts/cadastro.html')

    if len(senha) < 6: # Valida tamanho da senha
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais.')
        return render(request, 'accounts/cadastro.html')

    if len(usuario) < 6: # Valida tamanho do usuário
        messages.error(request, 'Usuário precisa ter 6 caracteres ou mais.')
        return render(request, 'accounts/cadastro.html')

    if senha != senha2: # Senha diferente da Senha 2
        messages.error(request, 'Senhas não conferem.')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(username = usuario).exists(): # Se o usuário já existir na base de dados
        messages.error(request, 'Usuário já existe.')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(email = email).exists(): # Se o email já existir na base de dados
        messages.error(request, 'E-mail já existe.')
        return render(request, 'accounts/cadastro.html')

    messages.success(request, 'Registrado com sucesso. Utilize os campos abaixo para fazer login.') # Se passou validações sucesso

    user = User.objects.create_user(username = usuario, email = email, password = senha, first_name = nome, last_name = sobrenome) # Cria Usuário
    user.save() # Confirma o save

    return redirect('login') # Redireciona para a pagina de login

@login_required(redirect_field_name='login') # Esse decorator direciona para uma pagina se não estiver logado
def dashboard(request):
    if request.method != "POST":
        form = FormContato()
        return render(request, 'accounts/dashboard.html', {'form': form})

    form = FormContato(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar formulário.')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    descricao = request.POST.get('descricao')

    if len(descricao) < 5:
        messages.error(request, 'Descrição precisa ter mais que 5 caracteres.')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    form.save()

    messages.success(request, f'Contato {request.POST.get("nome")} salvo com sucesso.')

    return redirect('dashboard')
