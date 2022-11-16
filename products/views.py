from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Products
from products.serializers import ProductSerailizers

# Create your views here.

class AllProducts(APIView):
    
    def get(self, request):
        product_set = Products.objects.all()
        serialiizer = ProductSerailizers(product_set, many=True)
        return Response(serialiizer.data)


class ProductAPI(APIView):

    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            return Response({
                'message':'Product not exist or Invalid ID'
            })

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerailizers(product)
        return Response(serializer.data)

    def patch(self, request, pk):
        try :
            product = self.get_object(pk)
            serializer = ProductSerailizers(product, data=request.data, partial=True)

            if not serializer.is_valid():
                return Response({
                    'errors':serializer.errors,
                    'message': 'Invalid input'
                })

            serializer.save()
            return Response({
                'payload': serializer.data,
                'message':'Data Updated'
            })
        
        except Exception as e:
            print(e)
            return Response({
                'message':'Invalid Data'
            })

    def delete(self, request, pk):
        try:
            product = self.get_object(pk)
            product.delete()
            return Response({
                'message':'Deleted'
            })
        except Exception as e:
            return Response({
                'message':'Invalid Id'
            })


class CreateProductAPI(APIView):
    def post(self, request):
        serializer = ProductSerailizers(data = request.data)

        if not serializer.is_valid():
            return Response({
                'errors': serializer.errors,
                'message': 'Invalid data provided'
            })

        serializer.save()
        return Response({
            'payload':serializer.data,
            'messaage':'Data added successfully'
        })
