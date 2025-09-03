from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406407360',
        'name': 'Haikal Muzaki',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)

# Create your views here.
