from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    LandingContent, VideoSection, Publication, SpokenWord, MinistryBrand, PhotoGallery
)
from .serializers import (
    LandingContentSerializer, VideoSectionSerializer,
    PublicationSerializer, SpokenWordSerializer,
    MinistryBrandSerializer, PhotoGallerySerializer
)

@api_view(['GET'])
def homepage_view(request):
    landing = LandingContent.objects.last()
    video = VideoSection.objects.last()
    publications = Publication.objects.order_by('-date')[:3]
    spoken_words = SpokenWord.objects.order_by('-date')[:3]
    brands = MinistryBrand.objects.all()
    gallery = PhotoGallery.objects.order_by('-uploaded_at')[:6]

    return Response({
        'landing': LandingContentSerializer(landing).data if landing else None,
        'featured_video': VideoSectionSerializer(video).data if video else None,
        'latest_publications': PublicationSerializer(publications, many=True).data,
        'spoken_words': SpokenWordSerializer(spoken_words, many=True).data,
        'ministry_brands': MinistryBrandSerializer(brands, many=True).data,
        'photo_gallery': PhotoGallerySerializer(gallery, many=True).data,
    })