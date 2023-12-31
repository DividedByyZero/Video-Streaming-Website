from django.urls import path
from VideoSystem import views
app_name = 'VideoSystem_APP'
urlpatterns = [
    path('uploadvideo/',views.Upload_Video.as_view(),name='UploadVideo'),
    path('videolist/',views.Video_list.as_view(),name='VideoList'),
    path('videoview/<slug:slug>/',views.VideoView,name='VideoView'),
    path('search/',views.Video_search,name='SearchVideo'),
]