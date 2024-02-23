from django.shortcuts import render,redirect
from TodoApp.models import Product
from.models import Cart
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def addcart(req,id):
    user=req.session['user']
    product=Product.objects.get(id=id)
    print(product)
    try:
        cart=Cart.objects.get(product=product)
        if cart.quantity<cart.product.stock:
            cart.quantity+=1
            cart.save()
    except Cart.DoesNotExist:
        cart=Cart.objects.create(user=user,product=product,quantity=1)
    return redirect('cartapp:displaycart')

def displaycart(req):
    user=req.session['user']
    cart=Cart.objects.all().filter(user=user)
    total=sum(cart.product.price * cart.quantity for cart in cart) - 1020
    return render(req,'cart.html',{'cart':cart,'total':total})




def removecart(req,id):
    user=req.session['user']
    product=Product.objects.get(id=id)
    cart=Cart.objects.get(product=product,user=user)
    if cart.quantity>1:
        cart.quantity-=1
        cart.save()
    return redirect('cartapp:displaycart')
    

def fullremove(req,id):
    user=req.session['user']
    product=Product.objects.get(id=id)
    cart=Cart.objects.get(product=product,user=user)
    cart.delete()
    return redirect('cartapp:displaycart')


def placeorder(req):
    user=req.session['user']
    cart=Cart.objects.filter(user=user)
    for cart in cart:
        prod=Product.objects.get(id=cart.product.id)
        prod.stock-=cart.quantity
        prod.save()
        cart.delete()
    return redirect('shop:home')