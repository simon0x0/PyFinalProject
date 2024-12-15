from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    url = models.URLField()
    pic = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return self.name