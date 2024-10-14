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
    FAQCategory, Projects, Achievements,ManualWebsite
)


class FAQCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class ManualWebsiteTranslationOptions(TranslationOptions):
    fields = ('youtube_link',)


class BannerTranslationOptions(TranslationOptions):
    fields = ('text',)


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'content',)


class TeamTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position')


class PartnersTranslationOptions(TranslationOptions):
    fields = ('company_name',)


class CustomerOpinionTranslationOptions(TranslationOptions):
    fields = ('full_name', 'opinion')


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


class ProjectsTranslationOptions(TranslationOptions):
    fields = ('short_description', 'name')


class AchievementsOptions(TranslationOptions):
    fields = ('short_description',)


translator.register(Banner, BannerTranslationOptions)
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
translator.register(Projects, ProjectsTranslationOptions)
translator.register(Achievements, AchievementsOptions)
translator.register(ManualWebsite, ManualWebsiteTranslationOptions)
