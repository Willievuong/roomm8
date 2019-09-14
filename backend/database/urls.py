from django.conf.urls import url, include 
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (ProfileCreateView, ProfileDetailsView, TaskCreateView, TaskDetailsView, RoomCreateView, RoomDetailsView)

urlpatterns = {
    url(r'^profile/$', ProfileCreateView, name="profile"),
    url(r'^profile/(?P<pk>[0-9]+)/$',
        ProfileDetailsView, name="profile_details"),
    url(r'^task/$', TaskCreateView, name="task"),
    url(r'^task/(?P<pk>[0-9]+)/$',
        TaskDetailsView, name="task_details"),
    url(r'^room/$', RoomCreateView, name="room"),
    url(r'^room/(?P<pk>[0-9]+)/$',
        RoomDetailsView, name="room_details")
}