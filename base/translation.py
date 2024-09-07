from modeltranslation.translator import translator, TranslationOptions
from .models import (
    Banner,
    News,
    Time,
    CustomerOpinion,
    FAQ,
    AboutUs,
    OfficeAddress,
    ServicesCategory,
    Services,
    AdditionalLinks)


class BaseTranslationOptions(TranslationOptions):
    fields = ('text',)


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'content',)


class TimeTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position')


class CustomerOpinionTranslationOptions(TranslationOptions):
    fields = ('company_name', 'position', 'full_name', 'opinion')


class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


class AboutUsTranslationOptions(TranslationOptions):
    fields = ('about_us', 'our_goal')


class OfficeAddressTranslationOptions(TranslationOptions):
    fields = ('address_name',)


class ServicesCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class ServicesTranslationOptions(TranslationOptions):
    fields = ('name', 'content',)


class AdditionalLinksTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Banner, BaseTranslationOptions)
translator.register(News, NewsTranslationOptions)
translator.register(Time, TimeTranslationOptions)
translator.register(CustomerOpinion, CustomerOpinionTranslationOptions)
translator.register(FAQ, FAQTranslationOptions)
translator.register(AboutUs, AboutUsTranslationOptions)
translator.register(OfficeAddress, OfficeAddressTranslationOptions)
translator.register(ServicesCategory, ServicesCategoryTranslationOptions)
translator.register(Services, ServicesTranslationOptions)
translator.register(AdditionalLinks, AdditionalLinksTranslationOptions)
