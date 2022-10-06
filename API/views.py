
from  rest_framework  import status
from rest_framework.response import Response

from app . models  import *
from .serializer import *
from rest_framework.views import APIView


class Productviews(APIView):
    def get(self,request,data=None):
        if data == None:
            products = Product.objects.all()
            serializer = productserilizer(products,many=True)
        elif  data == "mobile":
            products = Product.objects.filter(category="M")
            serializer = productserilizer(products,many=True)
        elif  data == "leptop":
            products = Product.objects.filter(category="L")
            serializer = productserilizer(products,many=True)
        elif  data == "topwear":
            products = Product.objects.filter(category="TW")
            serializer = productserilizer(products,many=True)
        elif  data == "bottamwear":
            products = Product.objects.filter(category="BW")
            serializer = productserilizer(products,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK,)

     
'''

'''