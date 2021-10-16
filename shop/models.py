from django.db import models
from django.urls import reverse

class Category(models.Model):
    
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # always put args in list datatype specially for slug
        return reverse("shop:product_list_by_category", args=[self.slug])
        
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='products')
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True)
    image = models.ImageField(upload_to = 'products/%Y/%m/%d',blank=True)
    # if we don't use null=True if the value doesn't exist it will be saved as '' in database
    description = models.TextField(blank=True)
    # max_digit includes decimal places
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id,self.slug])
    