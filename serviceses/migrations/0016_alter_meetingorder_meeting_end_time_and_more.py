# Generated by Django 5.0.9 on 2024-10-11 22:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceses', '0015_alter_meetingorder_meeting_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingorder',
            name='meeting_end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 10, 11, 23, 11, 6, 93965), null=True, verbose_name='Время встречи'),
        ),
        migrations.AlterField(
            model_name='meetingorder',
            name='meeting_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 10, 11, 22, 41, 6, 93949), null=True, verbose_name='Время встречи'),
        ),
    ]
