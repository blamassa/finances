from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse("<h1>teste</h1>")
    return render(request, '../templates/budgetlite/index.html')