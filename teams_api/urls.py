from django.urls import path

from . import views

urlpatterns = [
  # /
  path('', views.home, name='home'),
  # TEMPORARY
  path('signin', views.sign_in, name='signin'),
  path('signout', views.sign_out, name='signout'),
  path('home', views.home, name='home'),
  path('callback', views.callback, name='callback'),
  path('calendar', views.calendar, name='calendar'),
  path('channels',views.channels, name='channels')
]