from django.shortcuts import render

# Create your views here.


def resite(request):
    return render(request, 'resite/resite.html')
