from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView,
                                CreateView, UpdateView,
                                DeleteView)
from .models import Log


def home(request):
    return render(request, 'logApp/home.html')

def logs(request):

    context = {
        'logs': Log.objects.all(),
        'title': 'Logs'
    }
    return render(request, 'logApp/logs.html', context)

class LogListView(ListView):
    model = Log
    template_name = 'logApp/logs.html'
    context_object_name = 'logs'
    ordering = ['-event_datetime']
    paginate_by = 5

class LogDetailView(DetailView):
    model = Log

class LogCreateView(LoginRequiredMixin, CreateView):
    model = Log
    fields = ['location', 'comment']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class LogUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Log
    fields = ['location', 'comment']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        log = self.get_object()
        if self.request.user == log.author:
            return True
        return False

class LogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Log
    success_url = '/logs/'
    
    def test_func(self):
        log = self.get_object()
        if self.request.user == log.author:
            return True
        return False