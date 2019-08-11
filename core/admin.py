from django.contrib import admin
from .models import Subscribe, Event, EventImage, EventVideo, OurCause, OurReach, BannerImage, CauseContent, \
    RequestITTrainingContent, PartnersAndSponsorContent, PartnersAndSponsor, Header
from image_cropping.admin import ImageCroppingMixin


class EventImageInline(ImageCroppingMixin, admin.TabularInline):
    model = EventImage


class EventVideoInline(admin.TabularInline):
    model = EventVideo


class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline, EventVideoInline]


admin.site.register(Event, EventAdmin)


class BannerCropAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


admin.site.register(BannerImage, BannerCropAdmin)
admin.site.register(Subscribe)
admin.site.register(OurReach)
admin.site.register(OurCause)
admin.site.register(CauseContent)
admin.site.register(RequestITTrainingContent)
admin.site.register(PartnersAndSponsor)
admin.site.register(PartnersAndSponsorContent)
admin.site.register(Header)


