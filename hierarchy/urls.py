from django.conf.urls import url,include
from .views import *

urlpatterns = [
    url(r'^$',Index.as_view(),name='index'),  
]
