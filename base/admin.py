from django.contrib import admin

from .models import (
    Banner, News, Team, Statistics, CustomerOpinion,
    FAQ, AboutUs, Info, OfficeAddress, ServicesCategory,
    Services, AdditionalLinks, Partners, FAQCategory, Projects, Achievements, AchievementsImages, ManualWebsite
)


@admin.register(ManualWebsite)
class ManualWebsiteAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(FAQCategory)
class FAQCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')
    search_fields = ('id', 'text')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_description', 'views_count', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'short_description')
    list_filter = ('views_count', 'is_published')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'position')
    list_display_links = ('id', 'full_name')
    search_fields = ('id', 'full_name', 'position')
    list_filter = ('position',)


@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('id', 'customers_number', 'services_number', 'service_indicator')
    list_display_links = ('id', 'customers_number', 'services_number', 'service_indicator')
    search_fields = ('id', 'customers_number', 'services_number', 'service_indicator')
    list_filter = ('customers_number', 'services_number', 'service_indicator')


@admin.register(CustomerOpinion)
class CustomerOpinionAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name',)
    list_display_links = ('id', 'full_name')
    search_fields = ('id', 'full_name',)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'is_published')
    list_display_links = ('id', 'question')
    search_fields = ('id', 'question')


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'our_goal')
    list_display_links = ('id', 'our_goal')
    search_fields = ('id', 'our_goal')


class OfficeAddressAdmin(admin.TabularInline):
    model = OfficeAddress
    extra = 1


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'telegram', 'linkedin')
    list_display_links = ('id', 'phone_number', 'telegram')
    search_fields = ('id', 'phone_number', 'telegram', 'linkedin')
    inlines = (OfficeAddressAdmin,)


@admin.register(ServicesCategory)
class ServicesCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name')
    list_display_links = ('id', 'category', 'name')
    search_fields = ('id', 'name')
    list_filter = ('category',)


@admin.register(AdditionalLinks)
class AdditionalLinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_filter = ('is_published',)


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name')
    list_display_links = ('id', 'company_name')
    search_fields = ('id', 'company_name')


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_description')
    list_display_links = ('id', 'short_description')
    search_fields = ('id', 'short_description')


class AchievementsImagesAdmin(admin.TabularInline):
    model = AchievementsImages
    extra = 1


@admin.register(Achievements)
class AchievementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_description')
    list_display_links = ('id', 'short_description')
    inlines = (AchievementsImagesAdmin,)
