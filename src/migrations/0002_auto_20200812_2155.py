# Generated by Django 2.2.10 on 2020-08-12 21:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ActvityPeriod',
            new_name='ActivityPeriod',
        ),
    ]
