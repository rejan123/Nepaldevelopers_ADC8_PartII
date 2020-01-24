from django.shortcuts import render,redirect
from .models import *
from django.core.files.storage import FileSystemStorage

# Create your views here.

def get_products(req):
    return render(req,'add_product.html')

def get_update_products(req,ID):
    product=Product.objects.get(id=ID)
    context={
        "product":product
    }
    return render(req,'update_product.html',context=context)

def post_add_product(req):
    product_name=req.POST['product_name']
    product_price=req.POST['product_price']
    product_model=req.POST['product_model']
    product_category=req.POST['product_category']
    product_gender=req.POST['product_gender']
    product_details=req.POST['product_details']

    product_pic=req.FILES['product_pic']

    fs=FileSystemStorage()
    filename=fs.save(product_pic.name,product_pic)

    url=fs.url(filename)

    product=Product(product_pic=url,product_name=product_name,product_price=product_price,product_model=product_model,product_category=product_category,product_gender=product_gender,product_details=product_details)
    product.save()

    return redirect('home')

def post_update_product(req,ID):
    product_name=req.POST['product_name']
    product_price=req.POST['product_price']
    product_model=req.POST['product_model']
    product_category=req.POST['product_category']
    product_gender=req.POST['product_gender']
    product_details=req.POST['product_details']

    product_pic=req.FILES['product_pic']

    fs=FileSystemStorage()
    filename=fs.save(product_pic.name,product_pic)

    url=fs.url(filename)

    product=Product.objects.get(id=ID)

    product.product_name=product_name
    product.product_pic=url
    product.product_price=product_price
    product.product_model=product_model
    product.product_gender=product_gender
    product.product_category=product_category
    product.product_details=product_details

    product.save()

    return redirect('home')

def post_delete_product(req,ID):
    product=Product.objects.get(id=ID)
    product.delete()
    return redirect('home')

    


