from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from django.shortcuts import get_object_or_404
from random import choice, sample
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import (
    LandingContent, VideoSection, SpeechContent, SpokenWord,
    MinistryBrand, PhotoGallery, PressReleaseContent, SpeechContent, WriteUpContent,
    Publication, SpokenWord, AboutSection
)
from .serializers import (
    LandingContentSerializer, VideoSectionSerializer, SpeechContentSerializer,
    SpokenWordSerializer, MinistryBrandSerializer, PhotoGallerySerializer, PressReleaseContentSerializer, SpeechContentSerializer,
    WriteUpContentSerializer, PublicationSerializer,
    SpokenWordSerializer, AboutSectionSerializer, PublicationDetailSerializer
)
from .serializers import PublicationSummarySerializer
from datetime import datetime
from rest_framework.filters import OrderingFilter


class HomepageAPIView(APIView):
    def get(self, request):
        data = {}

        # Random LandingContent
        landing_contents = list(LandingContent.objects.all())
        data['landing'] = LandingContentSerializer(choice(landing_contents)).data if landing_contents else None

        # Random VideoSection
        video_sections = list(VideoSection.objects.all())
        data['video'] = VideoSectionSerializer(choice(video_sections)).data if video_sections else None

        # Latest SpeechContent (3)
        speeches = SpeechContent.objects.order_by('-id')[:3]
        data['speeches'] = SpeechContentSerializer(speeches, many=True).data

        # Latest SpokenWords (3)
        spoken_words = SpokenWord.objects.order_by('-date')[:3]
        data['spoken_words'] = SpokenWordSerializer(spoken_words, many=True).data

        # All MinistryBrands
        brands = MinistryBrand.objects.all()
        data['brands'] = MinistryBrandSerializer(brands, many=True).data

        # 6 Random Galleries
        galleries = list(PhotoGallery.objects.all())
        random_galleries = galleries[:6] if len(galleries) <= 6 else sample(galleries, 6)
        data['gallery'] = PhotoGallerySerializer(random_galleries, many=True).data

        return Response(data, status=status.HTTP_200_OK)



class PressReleaseListView(ListAPIView):
    queryset = PressReleaseContent.objects.all().order_by('-id')
    serializer_class = PressReleaseContentSerializer

class SpeechContentListView(ListAPIView):
    queryset = SpeechContent.objects.all().order_by('-id')
    serializer_class = SpeechContentSerializer

class WriteUpContentListView(ListAPIView):
    queryset = WriteUpContent.objects.all().order_by('-id')
    serializer_class = WriteUpContentSerializer


class PublicationListView(ListAPIView):
    serializer_class = PublicationSummarySerializer
    filter_backends = [OrderingFilter]
    ordering = ['-date']  

    def get_queryset(self):
        year = self.request.query_params.get('year', datetime.now().year)
        return Publication.objects.filter(date__year=year).order_by('-date')
    




class PublicationDetailView(RetrieveAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationDetailSerializer


class SpokenWordListView(ListAPIView):
    queryset = SpokenWord.objects.all().order_by('-date')
    serializer_class = SpokenWordSerializer

class AboutSectionListView(ListAPIView):
    queryset = AboutSection.objects.all()
    serializer_class = AboutSectionSerializer