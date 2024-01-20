from rest_framework import serializers
from django.contrib.auth import get_user_model

from geopy.distance import geodesic

from .models import Details

User = get_user_model()


class DetailsSerializer(serializers.ModelSerializer):
    distance = serializers.DecimalField(required=False, decimal_places=3, max_digits=7)
    class Meta:
        model = Details
        fields = ['full_name', 'latitude', 'longitude', 'distance']


class UsersSerializer(serializers.ModelSerializer):
    details = DetailsSerializer(required=False)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'details']

    def create(self, validated_data):
        try:
            details = validated_data.pop('details')
            user = User.objects.create(**validated_data)
            start_coordinates = (details['latitude'], details['longitude'])  
            destination_coordinates = (-23.6241039,-46.7024343)
            distance = geodesic(start_coordinates, destination_coordinates).kilometers
            # import ipdb;ipdb.set_trace()
            details['distance'] = distance
            Details.objects.create(user=user, **details)
            return user
        except:
            raise serializers.ValidationError('Invalid data')


    def update(self, instance, validated_data):
        try:
            details_data = validated_data.pop('details', None)
            
            instance.email = validated_data.get('email', instance.email)
            instance.username = validated_data.get('username', instance.username)
            instance.save()

            if details_data:
                start_coordinates = (details_data['latitude'], details_data['longitude'])
                destination_coordinates = (-23.6241039, -46.7024343)
                distance = geodesic(start_coordinates, destination_coordinates).kilometers
                instance.details.full_name = details_data['full_name']
                instance.details.latitude = details_data['latitude']
                instance.details.longitude = details_data['longitude']
                instance.details.distance = distance
                instance.details.save()
            return instance
        except:
            raise serializers.ValidationError('Invalid data')