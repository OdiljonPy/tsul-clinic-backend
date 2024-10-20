# Generated by Django 5.0.9 on 2024-10-14 01:20

import datetime
import serviceses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceses', '0020_alter_meetingorder_meeting_end_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetinglocation',
            name='is_send_sms',
            field=models.BooleanField(default=False, verbose_name='Смс отправлен'),
        ),
        migrations.AlterField(
            model_name='meetingorder',
            name='meeting_end_time',
            field=models.TimeField(blank=True, default=serviceses.models.default_meeting_end_time, null=True, verbose_name='Время встречи'),
        ),
        migrations.AlterField(
            model_name='meetingorder',
            name='meeting_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 10, 14, 1, 20, 43, 312881, tzinfo=datetime.timezone.utc), null=True, verbose_name='Время встречи'),
        ),
    ]
