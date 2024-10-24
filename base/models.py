from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import CASCADE

from abstract_models import base_models
from base.utils import validate_video_file

CHOICE_PARTNERS = (
    (1, 'Юристы'),
    (2, 'Натарус'),
    (3, 'Аудиторы')
)


class ManualWebsite(base_models.BaseModel):
    youtube_link = models.URLField(verbose_name="Ютуб видео ссылка")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Правило прользования вебсайтом"
        verbose_name_plural = "Правила прользования вебсайтом"
        ordering = ('-created_at',)


class Banner(base_models.BaseModel):
    text = models.CharField(max_length=150, verbose_name="Текст")
    image = models.ImageField(upload_to='banners/', verbose_name="Изображение")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"
        ordering = ('-created_at',)


class News(base_models.BaseModel):
    title = models.TextField(max_length=250, verbose_name="Заголовок")
    short_description = models.TextField(max_length=350, verbose_name="Краткое описание")
    image = models.ImageField(upload_to='news/', verbose_name="Изображение")
    content = RichTextField(verbose_name="Содержание")
    views_count = models.IntegerField(default=0, verbose_name="Количество просмотров")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ('-created_at',)


class Team(base_models.BaseModel):
    full_name = models.CharField(max_length=150, verbose_name="Полное имя")
    position = models.CharField(max_length=255, verbose_name="Позиция")
    image = models.ImageField(upload_to='time/', verbose_name="Изображение")
    is_volunteer = models.BooleanField(default=False, verbose_name='является волонтером')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"
        ordering = ('-created_at',)


class Statistics(base_models.BaseModel):
    customers_number = models.PositiveIntegerField(verbose_name="Количество клиентов")
    services_number = models.PositiveIntegerField(verbose_name="Количество сервисов")
    service_indicator = models.PositiveIntegerField(verbose_name="Индикатор обслуживания")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Статистика"
        verbose_name_plural = "Статистики"
        ordering = ('-created_at',)


class CustomerOpinion(base_models.BaseModel):
    full_name = models.CharField(max_length=150, verbose_name="Полное имя")
    opinion = models.TextField(max_length=800, verbose_name="Мнение", null=True, blank=True)
    video = models.FileField(upload_to='customer_opinion/', verbose_name="Видео",
                             validators=[validate_video_file])

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Мнение клиента"
        verbose_name_plural = "Мнения клиентов"
        ordering = ('created_at',)


class FAQCategory(base_models.BaseModel):
    name = models.CharField(max_length=150, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория часто задаваемого вопроса"
        verbose_name_plural = "Категории часто задоваемых вопросов"
        ordering = ('-created_at',)


class FAQ(base_models.BaseModel):
    faq_category = models.ForeignKey(FAQCategory, on_delete=models.CASCADE,
                                     verbose_name="Категория ЧЗВ", related_name='faq_category')
    question = models.TextField(max_length=1000, verbose_name="Вопрос")
    answer = RichTextField(verbose_name="Ответ")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.question[:30]

    class Meta:
        verbose_name = "Часто задаваемый вопрос"
        verbose_name_plural = "Часто задаваемые вопросы"
        ordering = ('-created_at',)


class AboutUs(base_models.BaseModel):
    about_us = RichTextField(verbose_name="О нас")
    our_goal = models.TextField(max_length=500, verbose_name="Наши цели")
    image = models.ImageField(upload_to='about/', verbose_name="Изображение")

    def __str__(self):
        return self.about_us[:50]

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"
        ordering = ('-created_at',)


class Info(base_models.BaseModel):
    youtube = models.URLField(default='www.youtube.com', verbose_name="Ютуб")
    instagram = models.URLField(default='www.instagram.com', verbose_name="Инстаграм")
    twitter = models.URLField(default='www.twitter.com', verbose_name="ТикТок")
    linkedin = models.URLField(default='www.linkedin.com', verbose_name="Фейсбук")
    telegram = models.URLField(default='www.telegram.org', verbose_name="Телеграм")
    phone_number = models.CharField(max_length=50, verbose_name="Номер телефона")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Информация"
        verbose_name_plural = "Информации"
        ordering = ('-created_at',)


class OfficeAddress(base_models.BaseModel):
    info = models.ForeignKey(Info, on_delete=models.CASCADE, related_name='office_address',
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
        ordering = ('-created_at',)


class ServicesCategory(base_models.BaseModel):
    name = models.CharField(max_length=150, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория сервиса"
        verbose_name_plural = "Категории сервисов"
        ordering = ('-created_at',)


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
        ordering = ('-created_at',)


class AdditionalLinks(base_models.BaseModel):
    name = models.CharField(max_length=150, verbose_name="Название")
    url = models.URLField(verbose_name="url")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дополнительная ссылка"
        verbose_name_plural = "Дополнительные ссылки"
        ordering = ('-created_at',)


class Partners(base_models.BaseModel):
    company_name = models.CharField(max_length=150, verbose_name="Название компании", null=True, blank=True)
    image = models.ImageField(upload_to='partner/', verbose_name="Изображение")

    def __str__(self):
        return self.company_name or str(self.id)

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"
        ordering = ('-created_at',)


class Projects(base_models.BaseModel):
    name = models.TextField(max_length=255, verbose_name='название проекта', null=True, blank=True)
    short_description = models.TextField(max_length=350, verbose_name='краткое описание')
    image = models.ImageField(upload_to='project/', verbose_name='изображение')
    youtube_url = models.URLField(null=True, blank=True, verbose_name="Ютуб url")
    telegram_url = models.URLField(null=True, blank=True, verbose_name="Телеграм url")
    instagram_url = models.URLField(null=True, blank=True, verbose_name="Инстаграм url")
    website_url = models.URLField(null=True, blank=True, verbose_name="Вебсайт url")
    twitter_url = models.URLField(null=True, blank=True, verbose_name="ТикТок url")
    linkedin_url = models.URLField(null=True, blank=True, verbose_name="Фейсбук url")

    def __str__(self):
        return self.short_description

    class Meta:
        verbose_name = 'Проэкт'
        verbose_name_plural = 'Проэкты'
        ordering = ('-created_at',)


class Achievements(base_models.BaseModel):
    short_description = models.CharField(max_length=255, verbose_name='краткое описание')

    def __str__(self):
        return self.short_description

    @property
    def get_images(self):
        return self.achievementsimages_set.all()

    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"
        ordering = ('-created_at',)


class AchievementsImages(base_models.BaseModel):
    achievement = models.ForeignKey(Achievements, on_delete=CASCADE, verbose_name="Досижение")
    image = models.ImageField(upload_to='achievements/', verbose_name="Изображение")

    def __str__(self):
        return str(self.achievement.id)

    class Meta:
        verbose_name = "Изображение достижения"
        verbose_name_plural = "Изображения достижений"
        ordering = ('-created_at',)
