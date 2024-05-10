from django.urls import path
from apps.base.views import index,contact


urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact')
]
