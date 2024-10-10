from modeltranslation.translator import translator, TranslationOptions
from .models import (
    Banner,
    News,
    Team,
    CustomerOpinion,
    FAQ,
    AboutUs,
    OfficeAddress,
    ServicesCategory,
    Services,
    AdditionalLinks,
    Partners,
    FAQCategory
)

class FAQCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

class BaseTranslationOptions(TranslationOptions):
    fields = ('text',)


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'content',)


class TeamTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position')


class PartnersTranslationOptions(TranslationOptions):
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
translator.register(Team, TeamTranslationOptions)
translator.register(Partners, PartnersTranslationOptions)
translator.register(CustomerOpinion, CustomerOpinionTranslationOptions)
translator.register(FAQ, FAQTranslationOptions)
translator.register(AboutUs, AboutUsTranslationOptions)
translator.register(OfficeAddress, OfficeAddressTranslationOptions)
translator.register(ServicesCategory, ServicesCategoryTranslationOptions)
translator.register(Services, ServicesTranslationOptions)
translator.register(AdditionalLinks, AdditionalLinksTranslationOptions)
translator.register(FAQCategory, FAQCategoryTranslationOptions)
