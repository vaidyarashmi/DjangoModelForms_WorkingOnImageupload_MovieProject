from django.urls import path,include
from testapp import views

urlpatterns = [
    path('movie/',views.movie_view)
]