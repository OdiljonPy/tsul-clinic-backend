# Generated by Django 5.0.9 on 2024-10-11 01:59

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_partners_alter_customeropinion_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('name_uz', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('name_ru', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('name_en', models.CharField(max_length=150, null=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория часто задаваемого вопроса',
                'verbose_name_plural': 'Категории часто задоваемых вопросов',
                'ordering': ('created_at',),
            },
        ),
        migrations.RemoveField(
            model_name='customeropinion',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='customeropinion',
            name='company_name_ru',
        ),
        migrations.RemoveField(
            model_name='customeropinion',
            name='company_name_uz',
        ),
        migrations.RemoveField(
            model_name='customeropinion',
            name='image',
        ),
        migrations.RemoveField(
            model_name='customeropinion',
            name='position',
        ),
        migrations.RemoveField(
            model_name='customeropinion',
            name='position_ru',
        ),
        migrations.RemoveField(
            model_name='customeropinion',
            name='position_uz',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='about_us_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='О нас'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='our_goal_en',
            field=models.TextField(max_length=500, null=True, verbose_name='Наши цели'),
        ),
        migrations.AddField(
            model_name='additionallinks',
            name='name_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='banner',
            name='text_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='customeropinion',
            name='full_name_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Полное имя'),
        ),
        migrations.AddField(
            model_name='customeropinion',
            name='opinion_en',
            field=models.TextField(blank=True, max_length=800, null=True, verbose_name='Мнение'),
        ),
        migrations.AddField(
            model_name='customeropinion',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='customer_opinion/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_en',
            field=models.TextField(max_length=1000, null=True, verbose_name='Ответ'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_en',
            field=models.TextField(max_length=500, null=True, verbose_name='Вопрос'),
        ),
        migrations.AddField(
            model_name='news',
            name='content_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Содержание'),
        ),
        migrations.AddField(
            model_name='news',
            name='short_description_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='officeaddress',
            name='address_name_en',
            field=models.CharField(max_length=250, null=True, verbose_name='Название адреса'),
        ),
        migrations.AddField(
            model_name='partners',
            name='full_name_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Полное имя'),
        ),
        migrations.AddField(
            model_name='partners',
            name='position_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Позиция'),
        ),
        migrations.AddField(
            model_name='services',
            name='content_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Содержание'),
        ),
        migrations.AddField(
            model_name='services',
            name='name_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='servicescategory',
            name='name_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='team',
            name='full_name_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Полное имя'),
        ),
        migrations.AddField(
            model_name='team',
            name='is_volunteer',
            field=models.BooleanField(default=False, verbose_name='является волонтером'),
        ),
        migrations.AddField(
            model_name='team',
            name='position_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='customeropinion',
            name='opinion',
            field=models.TextField(blank=True, max_length=800, null=True, verbose_name='Мнение'),
        ),
        migrations.AlterField(
            model_name='customeropinion',
            name='opinion_ru',
            field=models.TextField(blank=True, max_length=800, null=True, verbose_name='Мнение'),
        ),
        migrations.AlterField(
            model_name='customeropinion',
            name='opinion_uz',
            field=models.TextField(blank=True, max_length=800, null=True, verbose_name='Мнение'),
        ),
        migrations.AddField(
            model_name='faq',
            name='faq_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faq_category', to='base.faqcategory', verbose_name='Категория ЧЗВ'),
        ),
    ]