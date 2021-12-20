from rest_framework import serializers
from django.contrib.auth import get_user_model

from accomodation.models import Accomodation, AccomodationImages
from reviews.models import Review

User = get_user_model()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('name', 'description', 'date')

class AccomodationImagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AccomodationImages
        fields = ('image_id',)

class AccomodationSerializer(serializers.ModelSerializer):
    images = AccomodationImagesSerializer(many=True, required=False)
    reviews = ReviewSerializer(many=True, required=False)

    class Meta:
        model = Accomodation
        fields = '__all__'
        extra_kwargs = {'agent': {'read_only':True}}


class UserSerializer(serializers.ModelSerializer):
    listings = AccomodationSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'phone', 'state', 'listings', 'rating', 'no_of_rating')
        extra_kwargs = {'password': {'write_only': True}, 'rating':{'read_only':True}, 'no_of_rating':{'read_only':True}}

    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            phone = validated_data['phone'],
            state = validated_data['state']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user