from django.shortcuts import render
from TodoApp.models import Product
from django.db.models import Q

# Create your views here.

def SearchResult(req):
    products=None
    query=None
    if 'q' in req.GET:
        query=req.GET.get('q')
        print(query)
        products=Product.objects.all().filter(Q(name__contains=query)| Q(desc__contains=query))
        return render(req,'search.html',{'query':query,'products':products})