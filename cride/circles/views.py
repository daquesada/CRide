
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def list_circles(request):
    return Response({'data':"hola"})