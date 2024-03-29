# Generated by Django 5.0.1 on 2024-01-14 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate_app', '0006_rooms_room_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenent_profile',
            name='email',
            field=models.EmailField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tenent_profile',
            name='password',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
