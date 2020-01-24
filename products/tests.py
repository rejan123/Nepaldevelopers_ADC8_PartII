from django.test import TestCase
from products.models import *
# Create your tests here.

class ModelTestCase(TestCase):

    def test_valid_price(self):
        prd=Product.objects.create(product_name="Nike",product_price=1500,product_model="SK-15",product_category="Shoes")
        self.assertTrue(prd.valid_price())
        
    def test_valid_model(self):
        prd=Product.objects.create(product_name="Nike",product_price=1500,product_model="SK-15",product_category="Shoes")
        self.assertTrue(prd.valid_model())
    
    def test_count_orders(self):
        user=User.objects.create(user_name="asish",user_email="asish@gmail.com",user_gender="male",user_age=20)
        order=Order.objects.create()

        order.user_order.add(user)

        self.assertEqual(user.count_orders(),1)
    
    def test_valid_user_name(self):
        user=User.objects.create(user_name="asish",user_email="asish@gmail.com",user_gender="male",user_age=20)
        self.assertTrue(user.valid_user_name())
    
    def test_valid_gender(self):
        user=User.objects.create(user_name="asish",user_email="asish@gmail.com",user_gender="male",user_age=20)
        self.assertEqual(user.valid_gender())

