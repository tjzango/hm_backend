from rest_framework import serializers
from .models import (
    LandingContent, VideoSection, SpeechContent, SpokenWord,
    MinistryBrand, PhotoGallery, PressReleaseContent, SpeechContent, WriteUpContent,
    Publication, SpokenWord, AboutSection
)

class LandingContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingContent
        fields = '__all__'

class VideoSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSection
        fields = '__all__'

class SpeechContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeechContent
        fields = '__all__'

class SpokenWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpokenWord
        fields = '__all__'

class MinistryBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinistryBrand
        fields = '__all__'

class PhotoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoGallery
        fields = '__all__'



class PressReleaseContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PressReleaseContent
        fields = '__all__'

class SpeechContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeechContent
        fields = '__all__'

class WriteUpContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WriteUpContent
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'

class SpokenWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpokenWord
        fields = '__all__'

class AboutSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSection
        fields = '__all__'
