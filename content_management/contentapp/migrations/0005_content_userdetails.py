# Generated by Django 4.2.4 on 2023-09-01 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contentapp', '0004_remove_content_userdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='userdetails',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contentapp.userdetails'),
        ),
    ]
