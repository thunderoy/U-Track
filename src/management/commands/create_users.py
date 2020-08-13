from django.contrib.auth.models import User
from ...models import UserProfile
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import names
from random import choice, randrange
import datetime

# Python file for custom management command to populate the database
# with dummy User and activity period data

class Command(BaseCommand):
	help = 'Create random users with activity periods'

	def add_arguments(self, parser):
		parser.add_argument('total', type=int, help='Number of users to be created')

	def handle(self, *args, **kwargs):
		total = kwargs['total']
		for i in range(total):
			user = User.objects.create_user(username=get_random_string(), password='Abhi@2020', first_name=names.get_first_name(), last_name=names.get_last_name())
			
			timezone = choice(['Australia/Melbourne', 'US/Eastern', 'Canada/Eastern', 'Asia/Kolkata', 'America/Los_Angeles'])
			up = UserProfile(user=user, timezone=timezone)
			up.save()

			month = randrange(1, 12)
			day = randrange(1, 29)
			hour = randrange(24)
			mint = randrange(59)
			date = datetime.datetime(2020, month, day, hour, mint)

			for _ in range(randrange(2, 6)):
				start_time = date
				end_time = start_time + datetime.timedelta(minutes=+randrange(1, 59))

				user.activityperiod_set.create(start_time=start_time, end_time=end_time)

				date = date + datetime.timedelta(days=+randrange(100))
				date = date + datetime.timedelta(hours=+randrange(24))
				date = date + datetime.timedelta(minutes=+randrange(60))