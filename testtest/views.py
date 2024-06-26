from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest
from .models import Invoice
from django.views.decorators.csrf import csrf_exempt
import datetime


# invoiceNumber = models.IntegerField(unique=True)
#     customerName = models.CharField(max_length=150)
#     billingAddress = models.TextField()
#     shippingAddress = models.TextField()
#     GSTIN = models.CharField(max_length=20)
#     TotalAmount = models.IntegerField()

@csrf_exempt
def create(request):
    if request.method == 'POST':
        model = Invoice
        # taking dummy values due to time constraint
        data = model(uuid = 143 , invoiceNumber = 12334 , customerName = 'rupesh' , billingAddress='indore', shippingAddress='pune' , GSTIN = 'sdfg' , TotalAmount = 1000)
        data.save()
        return HttpResponse("invoice generated successfully")
    else :
        return HttpResponseBadRequest("invalid method")

@csrf_exempt
def update(request):
    if request.method == 'PUT':
        return HttpResponse("create")
    else :
        return HttpResponseBadRequest("invalid method")


@csrf_exempt
def delete(request):
    if request.method == 'DELETE':
        return HttpResponse("create")
    else :
        return HttpResponseBadRequest("invalid method")


def retrieve(request):
    if request.method == 'GET':
        data = Invoice.objects.all().values()
        datalist = [x for x in data]
        response = {
            "invoice-count": len(datalist),
            "data": datalist
        }
        return HttpResponse(str(response), content_type="application/json")
    else :
        return HttpResponseBadRequest("invalid method")


# priyanshu.b@altiushub.com
# balaji.b@altiushub.com

# Create your views here.
