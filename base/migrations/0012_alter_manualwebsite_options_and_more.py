# Generated by Django 5.0.9 on 2024-10-11 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_achievements_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manualwebsite',
            options={'verbose_name': 'Правило прользования вебсайтом', 'verbose_name_plural': 'Правила прользования вебсайтом'},
        ),
        migrations.AlterField(
            model_name='manualwebsite',
            name='youtube_link',
            field=models.URLField(verbose_name='Ютуб видео ссылка'),
        ),
    ]