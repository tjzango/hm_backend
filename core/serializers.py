from rest_framework import serializers
from .models import (
    LandingContent, VideoSection, Publication, SpokenWord,
    MinistryBrand, PhotoGallery
)

class LandingContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingContent
        fields = ['landing_image', 'spoken_Landing', 'memorable_quote']

class VideoSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSection
        fields = ['title', 'video_path', 'date']

class PublicationSerializer(serializers.ModelSerializer):
    short_content = serializers.SerializerMethodField()

    class Meta:
        model = Publication
        fields = ['category', 'title', 'date', 'landing_image', 'short_content']

    def get_short_content(self, obj):
        return obj.content[:110] + "..." if len(obj.content) > 110 else obj.content

class SpokenWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpokenWord
        fields = ['title', 'landing_image', 'main_image', 'date', 'content']

class MinistryBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinistryBrand
        fields = ['name', 'image_path']

class PhotoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoGallery
        fields = ['image', 'uploaded_at']
