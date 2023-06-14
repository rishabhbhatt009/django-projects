from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
@api_view()
def product_list(request):

    if request.method == 'GET': 
        queryset = Product.objects.select_related('collection').all()[:10]
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)

        ### replacement for if(valid)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data
        return Response('Gotha')

        # if serializer.is_valid():
        #     serializer.validated_data
        #     return Response('Gotha')
        # else:
        #     return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view()
def product_details(request, id):

    # try : 
    #     product = Product.objects.get(pk=id)
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)
    
    # except Product.DoesNotExist : 
    #     return Response(status=status.HTTP_404_NOT_FOUND) 

    product = get_object_or_404(Product,pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)    

@api_view()
def collection_details(request, pk):
    return Response('hello MF !')

