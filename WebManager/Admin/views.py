from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {'boldmessage': "Bold Test"}

    return render(request, 'Admin/index.html', context_dict)