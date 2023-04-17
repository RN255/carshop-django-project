from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Car
from django.template import loader

# Create your views here.

# this is the longer way of doing things
# def index(request):
#     most_recent_list = Car.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("carshop/index.html")
#     context = {
#         "most_recent_list": most_recent_list,
#     }
#     return HttpResponse(template.render(context, request))

# the below is a shortcut
def index(request):
    most_recent_list = Car.objects.order_by("-pub_date")[:5]
    context = {"most_recent_list": most_recent_list}
    return render(request, "carshop/index.html", context)

# def detail(request, id):
#     return HttpResponse("You're looking at question %s." % id)

# def detail(request, id):
#     try:
#         car = Car.objects.get(pk=id)
#     except Car.DoesNotExist:
#         raise Http404("entry does not exist")
#     return render(request, "carshop/detail.html", {"car": car})

# shortcut, above are longer
def detail(request, id):
    car = get_object_or_404(Car, pk=id)
    return render(request, "carshop/detail.html", {"car": car})