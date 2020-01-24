from django.db import models


class Product(models.Model):
    product_pic=models.ImageField()
    product_name=models.TextField()
    product_price=models.IntegerField(max_length=50)
    product_model=models.TextField()
    product_category=models.TextField()
    product_gender=models.TextField()
    product_details=models.TextField()

    def __str__(self):
        return self.product_name

class User(models.Model):
    user_name=models.TextField()
    user_email=models.TextField()
    user_address=models.TextField()
    user_gender=models.TextField()
    user_age=models.IntegerField(max_length=50)
    products=models.ManyToManyField(Product)
   
    def __str__(self):
        return self.user_name


class Payment(models.Model):
    payment_name=models.TextField()
    payment_type=models.TextField()
    user_payment=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.payment_name
   


class Order(models.Model):
    order_name=models.TextField()
    order_type=models.TextField()
    order_date=models.IntegerField(max_length=50)
    user_order=models.ManyToManyField(User)

    def __str__(self):
        return self.order_name
    
    



class Invoice(models.Model):
    invoice_name=models.TextField()
    invoice_number=models.IntegerField(max_length=50)
    user_invoice=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.invoice_name

    




    