from django.urls import path,re_path
from django.conf.urls import include
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    re_path(r'^offcampusjobs/(?P<id>[^/]+)',views.job_notifications,name='job_notifications'),
    re_path(r'^solutions/(?P<id>[^/]+)',views.solution,name='solutions'),
    path('jobNotifications',views.jobNotifications,name='jobNotifications'),
    path('prev_coding_problems',views.prev_coding_problems,name="prev_coding_problems"),
    re_path(r'^prev_coding_questions/(?P<id>[^/]+)',views.coding_problems,name='solutions'),
    path('courses',views.courses,name="courses")
]
