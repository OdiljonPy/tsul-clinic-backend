# Generated by Django 5.1.1 on 2024-09-09 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_team_delete_time_alter_aboutus_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeropinion',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='customer_opinion/'),
        ),
    ]