from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import itertools
#model libraryden turer modelin btun ozellklerine sahiptir miras alacaktr
#inheritence iinit de tanitki diger yerlerden buna ulas


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

    class Meta:
        db_table = "urunler"
        verbose_name = "urun"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/product/detail/%i' %self.id   # bu admn panelde buton koyar tklaynca bu linke gdersn

    def save(self):
        if not self.id:
            self.slug = slugify(self.name)

            for slug_id in itertools.count(1):   # ayni urun isimleri slugda karsmasin diye
                if not Product.objects.filter(slug = self.slug).exists():
                    break
                self.slug = '%s-%d' %(self.slug, slug_id)
        super(Product, self).save()

    @property
    def summary(self):
        return self.content[:50]