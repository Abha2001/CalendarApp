from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .import views

app_name='cal'

urlpatterns=[
	path('',views.index,name='index'),
	path('Calendar/',views.CalendarView.as_view(),name='calendar'),
	path('event/new/',views.new_event,name='event_new'),
    path('event/<int:event_id>/edit/', views.edit_event,name='event_edit'),
	path('signup/',views.signup,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_views,name='logout'),
]