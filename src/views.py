from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer, ActivityPeriodSerializer

from .models import UserProfile, ActivityPeriod

@api_view(['GET'])
def userProfileList(request):
	users = User.objects.all()
	serializer = UserSerializer(users, many=True)
	return Response(serializer.data)
