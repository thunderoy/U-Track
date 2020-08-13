from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	timezone = models.CharField('Timezone', max_length=20)


class ActivityPeriod(models.Model):
	user =  models.ForeignKey(User, on_delete=models.CASCADE)
	start_time = models.DateTimeField('Start Time')
	end_time = models.DateTimeField('End Time')