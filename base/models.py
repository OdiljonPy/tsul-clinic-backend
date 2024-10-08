from ckeditor.fields import RichTextField
from django.db import models

from abstract_models import base_models

CHOICE_PARTNERS = (
    (1, 'Юристы'),
    (2, 'Натарус'),
    (3, 'Аудиторы')
)


class Banner(base_models.BaseModel):
    text = models.CharField(max_length=150, verbose_name="Текст")
    image = models.ImageField(upload_to='banners/', verbose_name="Изображение")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"
        ordering = ('created_at',)


class News(base_models.BaseModel):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    short_description = models.CharField(max_length=255, verbose_name="Краткое описание")
    image = models.ImageField(upload_to='news/', verbose_name="Изображение")
    content = RichTextField(verbose_name="Содержание")
    views_count = models.IntegerField(default=0, verbose_name="Количество просмотров")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ('created_at',)


class Team(base_models.BaseModel):
    full_name = models.CharField(max_length=150, verbose_name="Полное имя")
    position = models.CharField(max_length=255, verbose_name="Позиция")
    image = models.ImageField(upload_to='time/', verbose_name="Изображение")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"
        ordering = ('created_at',)


class Statistics(base_models.BaseModel):
    customers_number = models.PositiveIntegerField(verbose_name="Количество клиентов")
    services_number = models.PositiveIntegerField(verbose_name="Количество сервисов")
    service_indicator = models.PositiveIntegerField(verbose_name="Индикатор обслуживания")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Статистика"
        verbose_name_plural = "Статистики"
        ordering = ('created_at',)


class CustomerOpinion(base_models.BaseModel):
    company_name = models.CharField(max_length=100, verbose_name="Название компании")
    position = models.CharField(max_length=150, verbose_name="Позиция")
    full_name = models.CharField(max_length=150, verbose_name="Полное имя")
    opinion = models.TextField(max_length=800, verbose_name="Мнение")
    image = models.ImageField(null=True, blank=True, upload_to='customer_opinion/', verbose_name="Изображение")

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Мнение клиента"
        verbose_name_plural = "Мнения клиентов"
        ordering = ('created_at',)


class FAQ(base_models.BaseModel):
    question = models.TextField(max_length=500, verbose_name="Вопрос")
    answer = models.TextField(max_length=1000, verbose_name="Ответ")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Часто задаваемый вопрос"
        verbose_name_plural = "Часто задаваемые вопросы"
        ordering = ('created_at',)


class AboutUs(base_models.BaseModel):
    about_us = RichTextField(verbose_name="О нас")
    our_goal = models.TextField(max_length=500, verbose_name="Наши цели")
    image = models.ImageField(upload_to='about/', verbose_name="Изображение")

    def __str__(self):
        return self.about_us[:50]

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"
        ordering = ('created_at',)


class Info(base_models.BaseModel):
    youtube = models.URLField(default='www.youtube.com', verbose_name="Ютуб")
    instagram = models.URLField(default='www.instagram.com', verbose_name="Инстаграм")
    twitter = models.URLField(default='www.twitter.com', verbose_name="Твиттер")
    linkedin = models.URLField(default='www.linkedin.com', verbose_name="Линкедин")
    telegram = models.URLField(default='www.telegram.com', verbose_name="Телеграм")
    phone_number = models.CharField(max_length=50, verbose_name="Номер телефона")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Информация"
        verbose_name_plural = "Информации"
        ordering = ('created_at',)


class OfficeAddress(base_models.BaseModel):
    info = models.ForeignKey(Info, on_delete=models.CASCADE, related_name='office_address', null=True,
                             verbose_name="Информация")
    address_name = models.CharField(max_length=250, verbose_name="Название адреса")
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    phone = models.CharField(max_length=50, null=True, blank=True, verbose_name="Номер телефона")

    def __str__(self):
        return self.address_name

    class Meta:
        verbose_name = "Адрес офиса"
        verbose_name_plural = "Адреса офисов"
        ordering = ('created_at',)


class ServicesCategory(base_models.BaseModel):
    name = models.CharField(max_length=150, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория сервиса"
        verbose_name_plural = "Категории сервисов"
        ordering = ('created_at',)


class Services(base_models.BaseModel):
    category = models.ForeignKey(ServicesCategory, on_delete=models.CASCADE, verbose_name="Категория")
    name = models.CharField(max_length=150, verbose_name="Название")
    image = models.ImageField(upload_to='services/', verbose_name="Изображение")
    content = RichTextField(verbose_name="Содержание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"
        ordering = ('created_at',)


class AdditionalLinks(base_models.BaseModel):
    name = models.CharField(max_length=150, verbose_name="Название")
    url = models.URLField(verbose_name="url")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дополнительная ссылка"
        verbose_name_plural = "Дополнительные ссылки"
        ordering = ('created_at',)


class Partners(base_models.BaseModel):
    full_name = models.CharField(max_length=150, verbose_name="Полное имя")
    position = models.CharField(max_length=255, verbose_name="Позиция")
    image = models.ImageField(upload_to='partner/', verbose_name="Изображение")
    category = models.IntegerField(choices=CHOICE_PARTNERS, default=1)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"
        ordering = ('created_at',)
