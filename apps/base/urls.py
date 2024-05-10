from django.urls import path
from apps.base.views import index,contact,blog,blog_details


urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('blog_details/', blog_details, name='blog_details')
]
