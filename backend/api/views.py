import json
from products.models import Product
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
# Create your views here.

def api_home(request, *args, **kwargs):

    model_data = Product.objects.all().order_by('?').first()

    data = {}
    
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    
    data = dict(data)
    print("data => ", data)

    return JsonResponse(data) 