from django.shortcuts import render


def render_main_template(request):
    data = {
        'title': 'Main page',
        'values': [1, {0: 'lol'}, 4.1415926],
    }
    return render(request,'main/main.html', data)


def about(request):
    return render(request,'main/about.html', {'title': 'About'})

