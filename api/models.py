from django.db import models

class Seller(models.Model):
    seller_name = models.CharField(max_length=100)
    seller_email = models.EmailField()
    seller_phone_number = models.CharField(max_length=12)
    
    def __str__(self):
        return self.seller_name

class Category(models.Model):
    category_title = models.CharField(max_length=50)
    def __str__(self):
        return self.category_title

class Product(models.Model):
    category_id = models.ForeignKey(Category ,related_name='kategori' ,on_delete=models.CASCADE, )
    product_title = models.CharField(max_length=100)
    product_desc = models.TextField()
    product_image = models.ImageField(upload_to='images')
    product_price = models.IntegerField(default=0)
    product_stock = models.IntegerField(default=0)
    
    class Meta:
        unique_together = ['category_id', 'id']
        ordering = ['id']
    def __str__(self):
        return self.product_title