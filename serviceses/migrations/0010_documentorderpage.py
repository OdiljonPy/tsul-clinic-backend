# Generated by Django 5.0.9 on 2024-10-11 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceses', '0009_alter_contacts_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentOrderPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
