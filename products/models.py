from django.db import models


class Product(models.Model):
    product_pic=models.ImageField(null=True)
    product_name=models.TextField()
    product_price=models.IntegerField(max_length=50)
    product_model=models.TextField()
    product_category=models.TextField()
    product_gender=models.TextField(null=True)
    product_details=models.TextField(null=True)

    def __str__(self):
        return self.product_name
    
    def valid_price(self):
        return self.product_price>0
    
    def valid_model(self):
        return self.product_model!=""

class User(models.Model):
    user_name=models.TextField()
    user_email=models.TextField()
    user_address=models.TextField(null=True)
    user_gender=models.TextField()
    user_age=models.IntegerField(max_length=50)
    products=models.ManyToManyField(Product)
   
    def __str__(self):
        return self.user_name

    def count_orders(self):
        return self.orders.all().count()

    def valid_user_name(self):
        return self.user_name!=""
    
    def valid_gender(self):
        return self.user_gender=="male" or self.user_gender=="female"

class Payment(models.Model):
    payment_name=models.TextField()
    payment_type=models.TextField()
    user_payment=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.payment_name
   


class Order(models.Model):
    order_name=models.TextField()
    order_type=models.TextField()
    order_date=models.DateField(max_length=50,null=True)
    user_order=models.ManyToManyField(User,related_name="orders")

    def __str__(self):
        return self.order_name
    
    
    



class Invoice(models.Model):
    invoice_name=models.TextField()
    invoice_number=models.IntegerField(max_length=50)
    user_invoice=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.invoice_name

    




    