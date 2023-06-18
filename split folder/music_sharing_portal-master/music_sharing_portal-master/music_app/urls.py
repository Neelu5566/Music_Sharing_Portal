

from django.urls import path
from music_app import views

urlpatterns = [
    path('', views.home,name="home"),
     path('songs/', views.songs, name='songs'),
    path('upload/', views.song_upload, name='song_upload'),
    # path('upload/',views.upload_song,name="upload_song")

]
