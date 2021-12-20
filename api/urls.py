from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AccomodationImagesCreate, AccomodationImagesDelete, AccomodationViewSet, RateAgent, ReviewCreate, UserCreate, UserRetrieve

router = DefaultRouter()
router.register('accomodation', AccomodationViewSet, basename='accomodation')


urlpatterns = [
    path('accomodationimages/', AccomodationImagesCreate.as_view(), name="images"),
    path('accomodationimages/<str:pk>/', AccomodationImagesDelete.as_view(), name="images_delete"),
    path('reviews/', ReviewCreate.as_view(), name='reviews'),
    path('agents/', UserCreate.as_view(), name='agent_create'),
    path('agents/<int:pk>/', UserRetrieve.as_view(), name='agent_retrieve'),
    path('agents/<int:pk>/rate/<int:rate_pk>/', RateAgent.as_view(), name='rate_agent'),
]

urlpatterns += router.urls