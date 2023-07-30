from django.db import models
from django.contrib.auth.models import User

#abtract icin db de olusmayacaktır sdece alt classlar icin tnmlanruz
class Company(models.Model): # trettk modelden inheritence yptk
    name = models.CharField(verbose_name="isim", max_length=100)
    content = models.CharField(verbose_name="aciklama")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="sahip")
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

class BookCompany(Company):
    pass

class GameCompany(Company):
    pass

class Book(models.Model):
    name = models.CharField(max_length=100)
    page_count = models.PositiveSmallIntegerField()

class Intro(Book):    #burada one to one relation olustur book ile intro arasnda
    content = models.TextField()

class ProxyBook(Book):  #vekil snftr db de olsmaz
    class Meta:
        proxy = True
        ordering = ["name"]

        @property
        def short_name(self):
            return self.name[:10]

