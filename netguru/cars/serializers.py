from rest_framework import serializers
from .models import Car, Popular, Rating


#it Has GET POST and Delete function
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'model','avg_rating']
#For rate post
class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields=('car_id','rating')


    def to_representation(self, instance):
        self.fields['car_id'] = CarSerializer(read_only=True)
        return super(RateSerializer, self).to_representation(instance)


'''
# I will try take Popular without serilizer just use views
class PopularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Popular
        fields = ['id', 'make', 'model', 'rates_number','rates']
'''
'''
class PostSerializer(serializers.Serializer):
    make = serializers.CharField(max_length=100)
    model = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Car.objects.create(**validated_data)
    

'''

'''
#Maybe I will remove it.
class RateSerializer(serializers.Serializer):
    car_id = serializers.IntegerField()
    rating = serializers.IntegerField()

    def create(self, validated_data):
        return Rating.objects.create(**validated_data)

'''
'''
class PopularSerializer(serializers.Serializer):

    car_id = serializers.IntegerField()
    make =serializers.CharField(max_length=50)
    model =serializers.CharField(max_length=50)
    rates_number = serializers.FloatField(default=1)

    def create(self, validated_data):
        return Popular.objects.create(**validated_data)


    def update(self, instance, validated_data):
             instance.id = validated_data.get('id', instance.id)
             instance.rating = validated_data.get('rating', instance.rating)
             instance.save()
             return instance
'''
'''
class RateSerializer(serializers.Serializer):
     make = serializers.CharField(max_length=20, unique=False)
     model = serializers.CharField(max_length=20, unique=True)
     rating = serializers.FloatField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
#    rates_number = serializers.FloatField(default=0)
#   avg_rating = serializers.FloatField(default=0)

     def update(self, instance, validated_data):

         instance.rating=validated_data.get('rating', instance.rating)
         instance.save()
         return instance

'''
# it is a normal serializer but I prefer to use model Serializers.
# class CarSerializers(serializers.Serializer):
#    make = serializers.CharField(max_length=100)
#    model = serializers.CharField(max_length=100)
#   avg_rating = serializers.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(0)])

#   def create(self, validated_data):
#        return Car.objects.cretae(**validated_data)

#    def update(self, instance, validated_data):
#        instance.make = validated_data.get('make', instance.make)
#       instance.model = validated_data.get('model', instance.model)
#        instance.avg_rating = validated_data.get('avg_rating', instance.avg_rating)
#        instance.save()
