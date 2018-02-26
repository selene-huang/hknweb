# Generated by Django 2.0.2 on 2018-04-01 04:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('private', models.BooleanField(default=True, verbose_name='Private profile?')),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Phone number must be ten digits.', regex='^/([^\\d]*\\d){10}$/')])),
                ('resume', models.FileField(blank=True, upload_to='')),
                ('graduation_date', models.DateField()),
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
