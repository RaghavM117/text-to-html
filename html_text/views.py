from django.shortcuts import render
from .forms import CForm

def convertor(request):
    form = CForm()
    return render(request, 'index.html', {'form':form})


