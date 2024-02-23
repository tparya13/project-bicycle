from django.shortcuts import render,get_object_or_404
from .models import Product,Category
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def Home(request):
    return render(request,'index.html')


def bicycle(request,c_slug=None):
    c_page=None
    product_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        
        product_list=Product.objects.all().filter(category=c_page,available=True)
    else:
        product_list=Product.objects.all().filter(available=True) 
        #PAGINATOR
    
    paginator=Paginator(product_list,50)
    
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
        
    #FOR INAVLID PAGE AND EMPTY PAGE
    try:
        products=paginator.page(page)
    except(EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)
        
           
    return render(request,'bicycle.html',{'data':product_list,'category':c_page,'products':products})



def Details(req,id):
    data=Product.objects.get(id=id)
    return render(req,'details.html',{'data':data})


