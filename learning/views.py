from django.shortcuts import render
from django.http import HttpResponse

def example_view(request):
    #return HttpResponse("asdsad")
    return render(request = request, template_name="example/detail.html")