from django.shortcuts import render
from django.http import HttpResponse
from .models import kinmel 

# Create your views here.

def home(request):
    kinmel_objs = kinmel.objects.all()
    context = {'kinmels': kinmel_objs}
    return render(request, 'index.html', context = context)

def dajuvai(request, ):
    return render(request,'dajuvai.html',)

def vaishnab(request,):
    return render(request,'vaishnab.html')

def order_view(request):
    if request.method == 'POST':
        food_name = request.POST.get('food_name')
        food_price = request.POST.get('food_price')
        return render(request, 'order.html', {'food_name': food_name, 'food_price': food_price})
    else:
        return


