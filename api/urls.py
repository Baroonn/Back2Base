from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .views import AccomodationImagesCreate, AccomodationImagesDelete, AccomodationViewSet, RateAgent, ReviewCreate, UserListCreate, UserRetrieve
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title="Back2Base API",
        default_version='v1',
        description="A REST API for finding your dream accommodation.",
        # terms_of_service="https://www.jaseci.org",
        contact=openapi.Contact(email="bolubee95@gmail.com"),
        # license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
router = DefaultRouter()
router.register('accomodation', AccomodationViewSet, basename='accomodation')


urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),  #<-- Here
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  #<-- Here
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),  #<-- Here
    path('accomodationimages/', AccomodationImagesCreate.as_view(), name="images"),
    path('accomodationimages/<str:pk>/', AccomodationImagesDelete.as_view(), name="images_delete"),
    path('reviews/', ReviewCreate.as_view(), name='reviews'),
    path('agents/', UserListCreate.as_view(), name='agent_create'),
    # path('agents/view/', UserList.as_view(), name='user_list'),
    path('agents/<int:pk>/', UserRetrieve.as_view(), name='agent_retrieve'),
    path('agents/<int:pk>/rate/<int:rate_pk>/', RateAgent.as_view(), name='rate_agent'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls