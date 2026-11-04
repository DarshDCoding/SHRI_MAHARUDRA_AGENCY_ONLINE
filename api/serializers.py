from rest_framework import serializers

from products.models import HSN, ProductImages, Product, Company

class HSNSerializer(serializers.ModelSerializer):
    class Meta:
        model = HSN
        fields = "__all__"

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields= "__all__"

class ProductSerializer(serializers.ModelSerializer):
    ProductCompany = CompanySerializer(read_only= True)
    ProductHSN = HSNSerializer(read_only=True)
    Images = ProductImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['pk', 'name', 'packing', 'mrp', 'company']
        #TODO: add all the important fields