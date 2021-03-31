from django.urls import path,include
from rest_framework import routers
from .views import CoustmerViewset


router=routers.DefaultRouter()
router.register('coustmerapi/', CoustmerViewset)

urlpatterns = [
    path('',include(router.urls)),
  
]

