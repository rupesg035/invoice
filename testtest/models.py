from django.db import models

# Create your models here.
# Id: UUID
# Date: string (UTC)
# InvoiceNumber: number
# CustomerName: string
# BillingAddress: string
# ShippingAddress: string
# GSTIN: string
# TotalAmount: Decimal


class Invoice(models.Model):
    uuid = models.IntegerField(unique=True)
    # invoiceDate = models.DateTimeField()
    invoiceNumber = models.IntegerField(unique=True)
    customerName = models.CharField(max_length=150)
    billingAddress = models.TextField()
    shippingAddress = models.TextField()
    GSTIN = models.CharField(max_length=20)
    TotalAmount = models.IntegerField()

    
    def __str__(self):
        return f"{self.customerName} {self.TotalAmount}"