from django.shortcuts import render,redirect
from products.models import Product
# Create your views here.

def home(request):
     if not request.user.is_authenticated:
        return redirect('login')
     all_products=Product.objects.all()
     context={
          "products":all_products
     }
     return render(request, 'home.html',context=context)

def custom(request):
     return render(request, 'custom.html') 
   
def contact(request):
     return render(request, 'contact.html')

def store(request):
     return render(request, 'store.html')     

def search(request):
     return render(request, 'search.html')     

     