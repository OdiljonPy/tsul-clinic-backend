# Generated by Django 5.0.9 on 2024-10-12 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_customeropinion_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='название проекта'),
        ),
    ]
