from django.shortcuts import render
from .models import Entry

def render_main_template(request):
    data = {'entries': Entry.objects.order_by('time')}
    return render(request, 'main/main.html', data)


def about(request):
    return render(request, 'main/about.html', {'title': 'About'})

