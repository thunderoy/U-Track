from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, ActivityPeriod

class ActivityPeriodSerializer(serializers.ModelSerializer):
	
	start_time = serializers.DateTimeField(format='%b %d %Y %I:%M%p')
	end_time = serializers.DateTimeField(format='%b %d %Y %I:%M%p')

	class Meta:
		model = ActivityPeriod
		fields = ('start_time', 'end_time')
		ordered= ('start_time',)


class UserSerializer(serializers.ModelSerializer):
	
	user_id = serializers.IntegerField(source='id')
	real_name = serializers.CharField(source='get_full_name')
	tz = serializers.DateTimeField(source='userprofile.timezone')
	activity_periods = ActivityPeriodSerializer(source='activityperiod_set', many=True)

	class Meta:
		model = User
		fields = ('user_id', 'real_name', 'tz', 'activity_periods')
