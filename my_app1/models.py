from django.db import models
from django.urls import reverse

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} | {self.last_name}"
    

class ShopProduct(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    image = models.ImageField()
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product_detail_url',kwargs={'slug':self.slug})
    




# Create your models here.


