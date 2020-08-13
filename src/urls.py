from django.urls import path
from . import views

urlpatterns = [
	path('', views.userProfileList, name="user-list"),
]
