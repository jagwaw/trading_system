# stocks/views.py
from django.db.models import Sum, F
from .models import Order
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def place_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def portfolio_value(request):
    total_value = Order.objects.aggregate(total_value=Sum(F('quantity') * F('price')))['total_value']
    return Response({'total_value': total_value})
