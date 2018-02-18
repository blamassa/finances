from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse ('oi')
    return render(request, '../templates/home/index.html')