from django.shortcuts import render

from .serializer import ProductCategorySerializer, ProductSerializer, ProductModelSerializer
from .models import ProductCategory, Product

from rest_framework.views import APIView, Response
from rest_framework.viewsets import ViewSet, ModelViewSet


class ProdCatAv(APIView):

    def get(self, request, pk=None):
        if pk:
            PO = ProductCategory.objects.get(pk=pk)
            JSO = ProductCategorySerializer(PO)
            return Response(JSO.data)            

        else:
            PCO =  ProductCategory.objects.all()

            JSO = ProductCategorySerializer(PCO, many=True)
            return Response(JSO.data)

    def post(self, request):
        PCD = ProductCategorySerializer(data=request.data)

        if PCD.is_valid():
            PCD.save()
            return Response({
                "created": True,
                "message": "Object created successfully."
            })


        return Response({
                        "created": False,
                        "message": "Invalid Data!"
        })


    def put(self, request, pk):
        pk = request.data["id"]

        PO = ProductCategory.objects.get(pk=pk)

        PCD = ProductCategorySerializer(PO, data=request.data)

        if PCD.is_valid():
            PCD.save()
            return Response({
                "created": True,
                "message": "Object created successfully."
            })
        
        
        return Response({
                        "created": False,
                        "message": "Invalid Data!"
        })


    def patch(self, request, pk):
        pk = request.data["id"]

        PO = ProductCategory.objects.get(pk=pk)

        PCD = ProductCategorySerializer(PO, data=request.data, partial=True)

        if PCD.is_valid():
            PCD.save()
            return Response({
                "created": True,
                "message": "Object created successfully."
            })
        
        
        return Response({
                        "created": False,
                        "message": "Invalid Data!"
        })


    def delete(self, request, pk):

        ProductCategory.objects.get(pk=pk).delete()

        return Response(
            {
                "delete": True,
                "message": "Object id deleted."
            }
        )
        

class ProdVset(ViewSet):

    def list(self, request):
        PCO =  Product.objects.all()
        
        JSO = ProductSerializer(PCO, many=True)
        return Response(JSO.data)

    def retrieve(self, request, pk):
        PO = Product.objects.get(pk=pk)
        JSO = ProductSerializer(PO)
        return Response(JSO.data)
        

    def create(self, request):
        PDO = ProductSerializer(data=request.data)

        if PDO.is_valid():
            PDO.save()

            return Response({
                "cretaed":True,
            })

        return Response({
            "created": False,
            "message": "Invalid Data!"
        })

    def update(self, request, pk):
        pk = request.data["id"]
        
        PO = Product.objects.get(pk=pk)

        PCD = ProductSerializer(PO, data=request.data)

        if PCD.is_valid():
            PCD.save()
            return Response({
                "created": True,
                "message": "Object created successfully."
            })
        
        
        return Response({
                        "created": False,
                        "message": "Invalid Data!"
        })        

    def partial_update(self, request, pk):
        pk = request.data["id"]
        
        PO = Product.objects.get(pk=pk)

        PCD = ProductSerializer(PO, data=request.data, partial=True)

        if PCD.is_valid():
            PCD.save()
            return Response({
                "created": True,
                "message": "Object created successfully."
            })
        
        
        return Response({
                        "created": False,
                        "message": "Invalid Data!"
        })

    def destroy(self, request, pk):
        Product.objects.get(pk=pk).delete()
        
        return Response(
            {
                "delete": True,
                "message": "Object id deleted."
            }
        )   



class ProductModelVS(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer