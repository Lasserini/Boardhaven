from django.shortcuts import render

# Home App Views


def index(request):
    return render(request, 'home/index.html')
