from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from .models import Invoice
from django.views.decorators.csrf import csrf_exempt
import json
import datetime

@csrf_exempt
def create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            invoice = Invoice(
                uuid=data['uuid'],
                invoiceDate=datetime.datetime.strptime(data['invoiceDate'], '%Y-%m-%dT%H:%M:%S'),
                invoiceNumber=data['invoiceNumber'],
                customerName=data['customerName'],
                billingAddress=data['billingAddress'],
                shippingAddress=data['shippingAddress'],
                GSTIN=data['GSTIN'],
                TotalAmount=data['TotalAmount']
            )
            invoice.save()
            return JsonResponse({"message": "Invoice created successfully"}, status=201)
        except KeyError as e:
            return JsonResponse({"error": f"Missing field: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return HttpResponseBadRequest("Invalid method")

@csrf_exempt
def update(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            invoice_uuid = data['uuid']
            invoice = Invoice.objects.get(uuid=invoice_uuid)
            
            invoice.uuid = data.get('uuid', invoice.uuid)
            invoice.invoiceDate = datetime.datetime.strptime(data.get('invoiceDate', invoice.invoiceDate.strftime('%Y-%m-%dT%H:%M:%S')), '%Y-%m-%dT%H:%M:%S')
            invoice.invoiceNumber = data.get('invoiceNumber', invoice.invoiceNumber)
            invoice.customerName = data.get('customerName', invoice.customerName)
            invoice.billingAddress = data.get('billingAddress', invoice.billingAddress)
            invoice.shippingAddress = data.get('shippingAddress', invoice.shippingAddress)
            invoice.GSTIN = data.get('GSTIN', invoice.GSTIN)
            invoice.TotalAmount = data.get('TotalAmount', invoice.TotalAmount)
            
            invoice.save()
            return JsonResponse({"message": "Invoice updated successfully"}, status=200)
        except Invoice.DoesNotExist:
            return JsonResponse({"error": "Invoice not found"}, status=404)
        except KeyError as e:
            return JsonResponse({"error": f"Missing field: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return HttpResponseBadRequest("Invalid method")

@csrf_exempt
def delete(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            invoice_uuid = data['uuid']
            invoice = Invoice.objects.get(uuid=invoice_uuid)
            invoice.delete()
            return JsonResponse({"message": "Invoice deleted successfully"}, status=200)
        except Invoice.DoesNotExist:
            return JsonResponse({"error": "Invoice not found"}, status=404)
        except KeyError as e:
            return JsonResponse({"error": f"Missing field: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return HttpResponseBadRequest("Invalid method")

def retrieve(request):
    if request.method == 'GET':
        try:
            invoices = Invoice.objects.all().values()
            data_list = list(invoices)
            response = {
                "invoice-count": len(data_list),
                "data": data_list
            }
            return JsonResponse(response, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return HttpResponseBadRequest("Invalid method")
