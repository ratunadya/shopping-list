from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Ratu Nadya Anjania',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)