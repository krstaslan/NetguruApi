
from .serializers import CarSerializer,PostSerializer,RateSerializer

from rest_framework import viewsets

from .models import Car,Rating

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class CarGet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@api_view(['POST'])
def car_post(request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def rate_post(request):
        serializer = RateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def rateCalculate(request,id):
    rates=0
    rates=Rating.object.filter(id=id)+rates
    return Response(rates)




