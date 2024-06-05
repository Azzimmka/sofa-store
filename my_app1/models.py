from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} | {self.last_name}"


class PopularProduct(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.price}"


class Newsletter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def save(self):
        return self.name

