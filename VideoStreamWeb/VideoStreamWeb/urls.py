from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
import sys
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('LoginSystem.urls')),
    path('videos/',include(('VideoSystem.urls','VideoSystem_APP'), namespace='VideoSystem_APP')),
    path('',views.Home,name='home'),
]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)