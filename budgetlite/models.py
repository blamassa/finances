from django.db import models

# Create your models here.

tags = [
    ('gas', ('Gas')),
    ('food', ('Food')),
    ('fun', ('Fun')),
    ('extras', ('Extras')),
    ('contas', ('Contas')),
    ]

contas = [
    ('deb', ('Débito/Dinheiro')),
    ('cred',('Cartão de Crédito')),    
]

class Despesa(models.Model):
    valor = models.FloatField(max_length=25)
    obs = models.CharField(max_length=25)
    data = models.DateField()
    tag =  models.CharField(max_length=25, choices=tags)
    conta = models.CharField(max_length=25, choices=contas)

    def __str__(self):
        return self.tag