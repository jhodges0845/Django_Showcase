from django.shortcuts import render
from .models import Log


def home(request):
    return render(request, 'logApp/home.html')

def logs(request):

    context = {
        'logs': Log.objects.all(),
        'title': 'Logs'
    }
    return render(request, 'logApp/logs.html', context)
