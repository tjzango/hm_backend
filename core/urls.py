from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.HomepageAPIView.as_view(), name='homepage-api'),
    path('press-releases/', views.PressReleaseListView.as_view(), name='press-release-list'),
    path('speeches/', views.SpeechContentListView.as_view(), name='speech-list'),
    path('writeups/', views.WriteUpContentListView.as_view(), name='writeup-list'),
    path('publications/', views.PublicationListView.as_view(), name='publication-list'),
    path('spokenwords/', views.SpokenWordListView.as_view(), name='spokenword-list'),
    path('about/', views.AboutSectionListView.as_view(), name='about-section-list'),
]





