from rest_framework import serializers

from mainapp.models import Cart, Product, CartProduct



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name','description','price','articul')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('user_name','created_at','total_price','delivery_address')

class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ('product','cart','total_price','amount')