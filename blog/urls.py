
from django.urls import path
from .views import homepage_view,aboutPage_view

urlpatterns = [
    path('', homepage_view, name = "homePage-blog"),
    path('about/', aboutPage_view, name = "about-blog"),
]
