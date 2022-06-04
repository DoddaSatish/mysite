from django.urls import path,re_path
from django.conf.urls import include
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    re_path(r'^offcampusjobs/(?P<id>[^/]+)',views.job_notifications,name='job_notifications'),
    re_path(r'^solutions/(?P<id>[^/]+)',views.solution,name='solutions'),
    path('jobNotifications',views.jobNotifications,name='jobNotifications')
]
