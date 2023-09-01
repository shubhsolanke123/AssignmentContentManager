# Generated by Django 4.2.4 on 2023-09-01 03:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contentapp', '0002_content_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator(message='Please provide a valid email address.')])),
                ('password', models.CharField(max_length=128, validators=[django.core.validators.MinLengthValidator(8, message='Password must be at least 8 characters long.')])),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', message='First name should only contain alphabetic characters.')])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', message='Last name should only contain alphabetic characters.')])),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10, message='Phone number must be exactly 10 digits long.'), django.core.validators.RegexValidator('^\\d+$', message='Phone number should only contain numeric digits.')])),
                ('address', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('pincode', models.CharField(max_length=6, validators=[django.core.validators.MinLengthValidator(6, message='Pincode must be exactly 6 digits long.'), django.core.validators.RegexValidator('^\\d+$', message='Pincode should only contain numeric digits.')])),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='userdetails',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contentapp.userdetails'),
        ),
    ]
