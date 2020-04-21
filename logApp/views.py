from django.shortcuts import render

stored_logs = [
    {
        'author': 'admin',
        'comment': 'Test Comment 1',
        'event_datetime': '04-21-2020 13:15',
        'location': 'Area 1'
    },
    {
        'author': 'admin',
        'comment': 'Test Comment 2',
        'event_datetime': '04-21-2020 13:16',
        'location': 'Area 1'
    }
]

def home(request):
    return render(request, 'logApp/home.html')

def logs(request):
    context = {
        'logs': stored_logs,
        'title': 'Logs'
    }
    return render(request, 'logApp/logs.html', context)
