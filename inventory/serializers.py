from .models import Stock, Sale, IncomingStock
from rest_framework import serializers


class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock
        fields = ['key', 'name', 'quantity', 'available','mrp_price']


class SaleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sale
        fields = ['key', 'time', 'product_id', 'name', 'quantity', 'count','sell_price', 'total_price']

class IncomingStockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IncomingStock
        fields = ['key', 'time', 'product_id', 'name', 'quantity', 'count','mrp_price', 'total_price']