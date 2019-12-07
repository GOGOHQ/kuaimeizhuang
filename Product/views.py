# Create your views here.
from django.http import HttpResponse,JsonResponse

from .models import Product


def fetchProduct(request,id):
    product = Product.objects.get(id=id)
    json_dict = {}
    color_species_list = []
    json_dict["id"] = product.id
    json_dict["name"] = product.name
    json_dict["category"] = product.category.name
    json_dict["picUrl"] = product.picUrl
    json_dict["sketch"] = product.sketch
    json_dict['brand'] = product.brand.name
    json_dict['ebrand'] = product.brand.ename
    for color in product.colorspecies.all():
        color_dict = {}
        color_dict["id"] = color.id
        color_dict["r"] = color.r
        color_dict["g"] = color.g
        color_dict["b"] = color.b
        color_dict["name"] = color.name
        color_species_list.append(color_dict)
    json_dict['colorspecies'] = color_species_list
    return JsonResponse(json_dict,charset="utf-8")


def fetchProductList(request):
    json_list = []
    list = Product.objects.all()
    for item in list:
        json_dict = {}
        color_species_list = []
        json_dict["id"] = item.id
        json_dict["name"] = item.name
        json_dict["category"] = item.category.name
        json_dict["picUrl"] = item.picUrl
        json_dict["sketch"] = item.sketch
        json_dict['brand'] = item.brand.name
        json_dict['ebrand'] = item.brand.ename
        for color in item.colorspecies.all():
            color_dict = {}
            color_dict["id"] = color.id
            color_dict["r"] = color.r
            color_dict["g"] = color.g
            color_dict["b"] = color.b
            color_dict["name"] = color.name
            color_species_list.append(color_dict)
        json_dict['colorspecies'] = color_species_list
        json_list.append(json_dict)
    return HttpResponse(json_list)