# Generated by Django 2.2.8 on 2022-02-28 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_auto_20220227_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvp',
            name='google_calendar_event_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
