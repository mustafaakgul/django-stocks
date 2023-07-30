from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import itertools

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="urunismi", default="standarturun", blank=True, null=True, unique=True, editable=True,
                            db_index=True, db_column="isim", help_text="ürün ismi acklayici metin")
    content = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    stock_count = models.PositiveSmallIntegerField(verbose_name="stokadet")
    price = models.DecimalField(verbose_name="ürünfiyat", decimal_places=2, max_digits=10)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=50)
    product = models.ManyToManyField(Product, related_name="categories", related_query_name="category")

#burada CATEGORYPRODUCT DIYE OTOMATIK BIR TABLO OLUSACAK