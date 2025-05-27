from rest_framework import serializers
from .models import (
    LandingContent, VideoSection, SpeechContent, SpokenWord,
    MinistryBrand, PhotoGallery, PressReleaseContent, SpeechContent, WriteUpContent,
    Publication, SpokenWord, AboutSection
)
from django.urls import reverse


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



class PublicationSummarySerializer(serializers.ModelSerializer):
    snippet = serializers.SerializerMethodField()
    link = serializers.SerializerMethodField()

    class Meta:
        model = Publication
        fields = ['category', 'title', 'landing_image', 'date', 'snippet', 'link']

    def get_snippet(self, obj):
        return obj.content[:50] + '...' if obj.content else ''

    def get_link(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(reverse('publication-detail', args=[obj.pk]))
        return f'/publications/{obj.pk}/'
    

class PublicationDetailSerializer(serializers.ModelSerializer):
    related = serializers.SerializerMethodField()
    others = serializers.SerializerMethodField()

    class Meta:
        model = Publication
        fields = '__all__'  
        depth = 0

    def get_related(self, obj):
        related_qs = Publication.objects.filter(
            category=obj.category
        ).exclude(id=obj.id).order_by('?')[:3]
        return PublicationSummarySerializer(related_qs, many=True, context=self.context).data

    def get_others(self, obj):
        others_qs = Publication.objects.exclude(id=obj.id).order_by('?')[:3]
        return PublicationSummarySerializer(others_qs, many=True, context=self.context).data

