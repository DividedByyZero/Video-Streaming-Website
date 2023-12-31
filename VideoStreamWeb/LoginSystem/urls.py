from django.urls import path
from LoginSystem import views
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
urlpatterns = [
    path('signup/',views.SignUpUser,name='SignUpUser'),
    path('login/',views.LoginUser,name='LoginUser'),
    path('logout/',views.LogoutUser,name='LogoutUser'),
    path('profile/',views.ProfileUser,name='ProfileUser'),
    path('addprofile/',views.AddProfile,name='AddProfile'),
    path('updateuser/',views.UpdateUser,name='UpdateUser'),
]


