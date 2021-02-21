from django.urls import path
#from rest_framework.authtoken.views import obtain_auth_token

from .views import(
    PostCreateAPIView,
    PostListAPIView

)


urlpatterns = [
    
    
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('list/', PostListAPIView.as_view(), name='list'),
  
    
]
