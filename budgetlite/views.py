from django.shortcuts import render
from django.http import HttpResponse
from budgetlite.models import Despesa
# Create your views here.

def index(request):
    #return HttpResponse("<h1>teste</h1>")
    despesas = Despesa.objects.all()
    context = {'despesas' : despesas}
    return render(request, '../templates/budgetlite/index.html', context)