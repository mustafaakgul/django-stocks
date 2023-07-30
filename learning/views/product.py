from django.shortcuts import render
from django.views.decorators.http import require_http_methods,require_GET, require_POST
from learning.models import Product

#@require_GET sadece get izin vreceksek
@require_http_methods(['GET', 'POST'])    #bu methodn izin vrecegi htttp methodlari
def product(request, pk=None):
    queryset = Product.objects.get(pk = pk)
    content = {
        "pk" : pk
    }
    return render(request = request, template_name="product/detail.html", context = content)

def products(request):
    queryset = Product.objects.all()
    content = {
        "products" : queryset
    }
    return render(request=request, template_name="product/list.html", context=content)

def product_archieve(request, year=None, month=None):
    print(year)
    print(month)
    return render(request = request, template_name="product/archieve.html")