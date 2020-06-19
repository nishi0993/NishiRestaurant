from rest_framework import serializers
from Order.models import Place, Restaurant, Staff
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()
    class Meta:
        model = Restaurant
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer()
    class Meta:
        model = Staff
        fields = '__all__'