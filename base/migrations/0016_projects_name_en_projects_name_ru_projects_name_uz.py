# Generated by Django 5.0.9 on 2024-10-12 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_projects_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='name_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='название проекта'),
        ),
        migrations.AddField(
            model_name='projects',
            name='name_ru',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='название проекта'),
        ),
        migrations.AddField(
            model_name='projects',
            name='name_uz',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='название проекта'),
        ),
    ]