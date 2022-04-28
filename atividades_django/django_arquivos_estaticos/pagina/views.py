from django.shortcuts import render

def index(request):
    return render(request, 'pagina/index.html')

def sobre(request):
    return render(request, 'pagina/sobre.html')
