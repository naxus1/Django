from django.shortcuts import render

# Create your views here.
def funcion(request):
    return render(request, 'pagina.html', {'contextdata': 'sdfsdfsdfsdfsdf'})