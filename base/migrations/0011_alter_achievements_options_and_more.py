# Generated by Django 5.0.9 on 2024-10-11 22:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_manualwebsite'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='achievements',
            options={'ordering': ('created_at',), 'verbose_name': 'Достижение', 'verbose_name_plural': 'Достижения'},
        ),
        migrations.AlterModelOptions(
            name='achievementsimages',
            options={'ordering': ('created_at',), 'verbose_name': 'Изображение достижения', 'verbose_name_plural': 'Изображения достижений'},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'ordering': ('created_at',), 'verbose_name': 'Проэкт', 'verbose_name_plural': 'Проэкты'},
        ),
        migrations.AlterField(
            model_name='achievementsimages',
            name='achievement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.achievements', verbose_name='Досижение'),
        ),
        migrations.AlterField(
            model_name='achievementsimages',
            name='image',
            field=models.ImageField(upload_to='achievements/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='instagram_url',
            field=models.URLField(blank=True, null=True, verbose_name='Инстаграм url'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True, verbose_name='Линкедин url'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='telegram_url',
            field=models.URLField(blank=True, null=True, verbose_name='Телеграм url'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='twitter_url',
            field=models.URLField(blank=True, null=True, verbose_name='Твиттер url'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='website_url',
            field=models.URLField(blank=True, null=True, verbose_name='Вебсайт url'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='youtube_url',
            field=models.URLField(blank=True, null=True, verbose_name='Ютуб url'),
        ),
    ]
