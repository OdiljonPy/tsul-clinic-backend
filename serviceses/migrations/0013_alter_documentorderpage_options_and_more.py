# Generated by Django 5.0.9 on 2024-10-11 21:45

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceses', '0012_delete_manualwebsite_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documentorderpage',
            options={'ordering': ('created_at',), 'verbose_name': 'Страница заказа документа', 'verbose_name_plural': 'Страница заказов документов'},
        ),
        migrations.AlterField(
            model_name='complaint',
            name='complaint',
            field=models.TextField(verbose_name='Жалоба'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='order_document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceses.documentorder', verbose_name='Заказ документа'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='contacts/document/', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='documentorder',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='order/document/', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='documentorderpage',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активен'),
        ),
        migrations.AlterField(
            model_name='meetingorder',
            name='meeting_end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 10, 11, 22, 15, 11, 999467), null=True, verbose_name='Время встречи'),
        ),
        migrations.AlterField(
            model_name='meetingorder',
            name='meeting_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 10, 11, 21, 45, 11, 999451), null=True, verbose_name='Время встречи'),
        ),
    ]
