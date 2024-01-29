from django.shortcuts import render
from .models import Stock, Sale, IncomingStock
from rest_framework import viewsets
from .serializers import StockSerializer, SaleSerializer, IncomingStockSerializer
# Create your views here.

class StockView(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
