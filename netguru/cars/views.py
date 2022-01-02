from django.db.models import Avg
from rest_framework.views import APIView
from .serializers import CarSerializer, RateSerializer  # , PopularSerializer
from rest_framework import viewsets, authentication, generics
from .models import Car, Rating, Popular
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse


# bring all Car object
class CarGet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# for adding new Car object
@api_view(['POST'])
def car_post(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Delete(request, pid):
    try:
        car = Car.objects.get(pk=pid)
    except Car.DoesNotExist():
        return Response(status=status.HTTP_404_NOT_FOUND)

    car.delete()
    return HttpResponse(status=204)

# it need revision works for add rate
@api_view(['POST'])
def rate_post(request):
    serializer = RateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def rates(request):
        Rating.objects.order_by('-rating')
        rates = Rating.objects.all()
        serializer = RateSerializer(rates, many=True)
        return Response(serializer.data)
'''

@api_view(['DELETE'])
def car_delete(request, id):
    try:
        car = Car.objects.get(id=id)
    except Car.DoesNotExist():
        return Response(status=status.HTTP_404_NOT_FOUND)
    car.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

'''

'''
# Product Detail
def car_detail(request,id):
	car=Rating.objects.get(id=id)
	related_products=Rating.objects.filter(category=car.category).exclude(id=id)[:4]

	# Check
	canAdd=True
	reviewCheck=Rating.objects.filter(user=request.user,product=product).count()
	if request.user.is_authenticated:
		if reviewCheck > 0:
			canAdd=False
	# End

	# Fetch reviews
	reviews=ProductReview.objects.filter(product=product)
	# End

	# Fetch avg rating for reviews
	avg_reviews=Rating.objects.filter(car=car).aggregate(avg_rating=Avg('review_rating'))
	# End

	return render(request, 'product_detail.html',{'data':product,'related':related_products,'colors':colors,'sizes':sizes,'reviewForm':reviewForm,'canAdd':canAdd,'reviews':reviews,'avg_reviews':avg_reviews})
'''
'''
def car_detail(request,slug,id):
	car=Car.objects.get(id=id)
	related_products=Car.objects.filter(category=car.category).exclude(id=id)[:4]
	car_id=Rating.objects.filter(product=product).values('car_id__id','car_id__make','car_id__model').distinct()
#	sizes=ProductAttribute.objects.filter(product=product).values('size__id','size__title','price','color__id').distinct()
	reviewForm=ReviewAdd()

	# Check
	canAdd=True
	reviewCheck=ProductReview.objects.filter(user=request.user,product=product).count()
	if request.user.is_authenticated:
		if reviewCheck > 0:
			canAdd=False
	# End

	# Fetch reviews
	reviews=ProductReview.objects.filter(product=product)
	# End

	# Fetch avg rating for reviews
	avg_reviews=ProductReview.objects.filter(product=product).aggregate(avg_rating=Avg('review_rating'))
	# End

	return render(request, 'product_detail.html',{'data':product,'related':related_products,'colors':colors,'sizes':sizes,'reviewForm':reviewForm,'canAdd':canAdd,'reviews':reviews,'avg_reviews':avg_reviews})


def rateCalculate(request, id):
    rates = 0
    rates = Rating.object.filter(id=id) + rates
    return Response(rates)


'''


# Se

@api_view(['GET', 'PUT', 'DELETE'])
def Delete(request, pid):
    try:
        car = Car.objects.get(pk=pid)
    except Car.DoesNotExist():
        return Response(status=status.HTTP_404_NOT_FOUND)

    car.delete()
    return HttpResponse(status=204)



'''
def save_rate(request, pid):
    car = Car.objects.get(pk=pid)
    rating = Rating.objects.create(
        car=car,
        rating=request.POST['rating'],
    )
    data = {
        'id': car.pk,
        'make': car.make,
        'model': car.model,
        'rating': request.POST['rating']
    }

    # Fetch avg rating for reviews
    avg_reviews = Rating.objects.filter(car=car).aggregate(avg_rating=Avg('rating'))
    # End

    return Response({ 'data': data, 'avg_reviews': avg_reviews})
'''

'''
# for Popular list
class RateCount(APIView):

    def get(self):
        """
        Return a list of all cars and calculate total rate for all cars..
        """
        total = 0
        rate_number=0
        count = Car.objects.count()
        Rating.objects.order_by('car_id')
        for i in range(count):
            for rates in Rating.objects.all().filter(id__in=i):
                total += rates
                rate_number+=1
           #in here ı should update Popular Serilizer and
            #ı have to calculate avarage rate and update it in Car
            order = Popular(i, 'renato', 10.50, total,rate_number)
            serializer = PopularSerializer(order)

            serializer.data
            rates = [total]
            rate_number = 0
        return Response(rates)
'''
