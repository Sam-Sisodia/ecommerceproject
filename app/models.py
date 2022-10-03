
from django.db import models

# Create your models here.
from django.contrib.auth.models import User

STATE_CHOICES= (
    ('HARYANA','HARYANA'),
    ('DELHI','DELHI'),
    ('PUNJAB','PUNJAB'),
    ('BIHAR','BIHAR'),
    ( 'UP', 'UP'))


class  customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name  = models.CharField(max_length=20)
    locality = models.CharField(max_length=20)
    city  = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    state  = models.CharField(choices=STATE_CHOICES,max_length=20)

    def __str__(self):
        return str(self.id)



CATEGORY_CHOICES = (
    ('M','MOBILE'),
    ('L','LAPTOP'),
    ('TW','TOPWEAR'),
    ('BW', 'BOTTOWEAR')
)

class Product(models.Model):
    title = models.CharField(max_length=30)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    discription = models.TextField(max_length=500)
    brand = models.CharField(max_length=20)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=3)
    product_image=models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.id)



Status_Choices=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way', 'On the way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)


class OrderPlace(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date  = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=Status_Choices,max_length=10, default='Pending')



