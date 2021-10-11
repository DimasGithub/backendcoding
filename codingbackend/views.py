from django.shortcuts import render,redirect
def index(request):
    context = {
        'title':'Test Coding Backend',
    }
    return render(request, 'index.html', context)