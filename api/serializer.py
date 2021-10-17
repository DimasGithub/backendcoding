import math
import http.client
from api.models import Product, Category
from rest_framework import serializers

class ShippingSerializer(serializers.Serializer):
    origin = serializers.CharField()
    destination = serializers.CharField()
    price = serializers.IntegerField(default=0)
    weight = serializers.FloatField(default=0)
    qty = serializers.IntegerField(default=0)
    total = serializers.IntegerField(default=0)

    def round_up(n, decimals=0): 
        multiplier = 10 ** decimals 
        return math.ceil(n * multiplier) / multiplier

    def save(self):
        qty = self.validated_data['qty']
        weight = self.validated_data['weight'] 
        totalweight = qty * weight / 1000
        if totalweight <= 1:
            totalweight = 1
        elif totalweight > 1:
            belakangkoma = round(totalweight % 1, 2)
            if belakangkoma <= 0.5:
                totalweight = round(totalweight, 0) + 0.5
            elif belakangkoma > 0.5:
                totalweight = round(totalweight, 0)
        print('total berat = ' + str(totalweight)+ 'kg')
        origin = self.validated_data['origin']
        if origin == 'China':
            price_origin = 150000 * totalweight
            print('Biaya kirim dari China = '+ str(price_origin))
        elif origin == 'Amerika':
            price_origin = 200000 * totalweight
            print('Biaya kirim dari Amerika = '+ str(price_origin))
        destination = self.validated_data['destination']
        if destination == 'Jawa':
            price_destination = 20000 * totalweight
            print('Biaya kirim ke Jawa = '+ str(price_destination))
        elif destination == 'Luar Jawa':
            price_destination = 50000 * totalweight
            print('Biaya kirim ke Luar Jawa = '+ str(price_destination))
        print('biaya total ongkir = '+ str(price_destination+price_origin))
        price = self.validated_data['price']
        subtotal = price * qty
        print('subtotal barang = '+ str(subtotal))
        bea = (7.5 / 100) * subtotal
        print('bea = '+ str(bea))
        ppn = (10/100) * subtotal
        print('ppn = '+ str(ppn))
        pph = (5 /100 )* subtotal
        print('pph = '+str(pph))
        tax = bea + ppn + pph
        print('tax = '+ str(tax))
        totalprice = price_destination + price_origin + tax + subtotal
        print('total biaya non admin = '+ str(totalprice))
        priceadm = (5/100) * totalprice
        totalseluruh = totalprice + priceadm
        print('total biaya + admin = '+ str(totalseluruh))
        return totalseluruh

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    categoryku  = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'