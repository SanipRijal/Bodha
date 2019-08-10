from django.contrib import admin
from .models import Subscribe, Event, EventImage, EventVideo, OurCause, OurReach, BannerImage


class EventImageInline(admin.TabularInline):
    model = EventImage


class EventVideoInline(admin.TabularInline):
    model = EventVideo


class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline, EventVideoInline]


admin.site.register(Event, EventAdmin)
admin.site.register(BannerImage)
admin.site.register(Subscribe)
admin.site.register(OurReach)
admin.site.register(OurCause)

