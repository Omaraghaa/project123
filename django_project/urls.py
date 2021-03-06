"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
#from teams_api import views as teams_views
from teams_api import views as teams_api
#from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('dashboard/', user_views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('blog.urls')),
    #path('msteams/', teams_views.msteams, name='msteams'),
    path('msteams_login/', teams_api.home , name='msteams_login'),
    #path('blog_home/', blog_views.sign_out, name='signout'),
    path('', include('teams_api.urls')),
    path('search',include('search.urls')),
    path('FDA',include('FDA.urls')),
    path('researchGrants',include('researchGrants.urls')),
    path('get_linkedin_auth/', user_views.linkedin_auth, name='get_linkedin_auth'),
    path('linkedin_usr_info_call/', user_views.linkedin_usr_info, name='linkedin_usr_info_call'),
    path('tgasearch',include('tgasearch.urls')),
    path('ema',include('ema.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
