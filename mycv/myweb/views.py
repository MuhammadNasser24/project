from django.shortcuts import render

def show_view(request):
    return render(request, 'show.html')
