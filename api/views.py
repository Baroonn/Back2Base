from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

from accomodation.models import Accomodation, AccomodationImages
from reviews.models import Review

from .serializers import AccomodationImagesSerializer, AccomodationSerializer, ReviewSerializer, UserSerializer

# Create your views here.
class AccomodationViewSet(viewsets.ModelViewSet):
    serializer_class = AccomodationSerializer

    def get_queryset(self):
        queryset = Accomodation.objects.all()
        state = self.request.query_params.get('state')
        query_lga = self.request.query_params.get('lga')
        query_category = self.request.query_params.get('category')
        query_status = self.request.query_params.get('status')
        if state is not None:
            queryset = queryset.filter(agent__state = state)
        if query_lga is not None:
            queryset = queryset.filter(lga = query_lga)
        if query_category is not None:
            queryset = queryset.filter(category = query_category)
        if query_status is not None:
            queryset = queryset.filter(status = query_status)
        return queryset
        

class AccomodationImagesCreate(generics.CreateAPIView):
    queryset = AccomodationImages.objects.all()
    serializer_class = AccomodationImagesSerializer

class AccomodationImagesDelete(generics.DestroyAPIView):
    queryset = AccomodationImages.objects.all()
    serializer_class = AccomodationImagesSerializer

class ReviewCreate(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RateAgent(APIView):
    def get(self, request, pk, rate_pk):
        if not 0<=rate_pk<=5:
            return Response({'detail':'rate not valid'})
        agent = get_object_or_404(User, pk=pk)
        total_rating = agent.total_rating
        no_of_rating = agent.no_of_rating
        if agent.no_of_rating == 0:
            agent.rating = rate_pk
        else:
            agent.rating = (agent.total_rating + rate_pk) / (agent.no_of_rating+1)
        no_of_rating += 1
        agent.total_rating += rate_pk 
        agent.no_of_rating += 1
        agent.save()
        data = UserSerializer(agent).data
        return Response(data)