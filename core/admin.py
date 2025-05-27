from django.contrib import admin
from .models import (
    LandingContent, VideoSection, PhotoGallery, PressReleaseContent, 
    SpeechContent, WriteUpContent, MinistryBrand, Publication,
    SpokenWordsCat, SpokenWord, AboutSection
)

class VideoSectionInline(admin.TabularInline):
    model = VideoSection
    extra = 1

class PhotoGalleryInline(admin.TabularInline):
    model = PhotoGallery
    extra = 1

@admin.register(LandingContent)
class LandingContentAdmin(admin.ModelAdmin):
    inlines = [VideoSectionInline, PhotoGalleryInline]
    list_display = ('id', 'memorable_quote')

admin.site.register(PressReleaseContent)
admin.site.register(SpeechContent)
admin.site.register(WriteUpContent)
admin.site.register(MinistryBrand)
admin.site.register(Publication)
admin.site.register(SpokenWordsCat)
admin.site.register(SpokenWord)
admin.site.register(AboutSection)
