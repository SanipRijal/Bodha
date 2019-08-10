from django.contrib import admin
from .models import Subscribe, Event, EventImage, EventVideo, OurCause, OurReach, BannerImage
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

