from ckeditor.fields import RichTextField
from django.db import models

from abstract_models import base_models


class Banner(base_models.BaseModel):
    text = models.CharField(max_length=150)
    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return self.text


class News(base_models.BaseModel):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=150)
    image = models.ImageField(upload_to='news/')
    content = RichTextField()
    views_count = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Time(base_models.BaseModel):
    full_name = models.CharField(max_length=150)
    position = models.CharField(max_length=50)
    image = models.ImageField(upload_to='time/')

    def __str__(self):
        return self.full_name


class Statistics(base_models.BaseModel):
    customers_number = models.PositiveIntegerField()
    services_number = models.PositiveIntegerField()
    service_indicator = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)


class CustomerOpinion(base_models.BaseModel):
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    full_name = models.CharField(max_length=150)
    opinion = models.CharField(max_length=150)

    def __str__(self):
        return self.company_name


class FAQ(base_models.BaseModel):
    question = models.CharField(max_length=150)
    answer = models.CharField(max_length=1000)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.question


class AboutUs(base_models.BaseModel):
    about_us = RichTextField()
    our_goal = models.TextField(max_length=500)
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.about_us[:50]


class Info(base_models.BaseModel):
    youtube = models.URLField(default='www.youtube.com')
    instagram = models.URLField(default='www.instagram.com')
    twitter = models.URLField(default='www.twitter.com')
    linkedin = models.URLField(default='www.linkedin.com')
    telegram = models.URLField(default='www.telegram.com')
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)


class OfficeAddress(base_models.BaseModel):
    info = models.ForeignKey(Info, on_delete=models.CASCADE, related_name='office_address', null=True)
    address_name = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()
    phone = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.address_name


class ServicesCategory(base_models.BaseModel):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Services(base_models.BaseModel):
    category = models.ForeignKey(ServicesCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='services/')
    content = RichTextField()

    def __str__(self):
        return self.name


class AdditionalLinks(base_models.BaseModel):
    name = models.CharField(max_length=150)
    url = models.URLField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name
