from django.shortcuts import render

# Create your views here.

def home(request):
    # nome = 'Davi'
    # conhecimentos = ['HTML', 'CSS', 'JavaScript', 'Python', 'Django', 'Git']

    eu = {
        'nome' : 'Davi',
        'Altura': 1.75,
        'Conhecimentos': ['HTML', 'CSS', 'JavaScript', 'Python', 'Django', 'Git']
        
    }

    return render(request, 'index.html', {'conhecimentos': conhecimentos, 'nome': nome})