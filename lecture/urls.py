from django.conf.urls import url
from .views import LectureList, LectureDetail, LectureCreate,LectureSearchList, LectureUpdate

urlpatterns = [
  url(r'^list/$',LectureList.as_view(),name='list'),
  url(r'^create/$',LectureCreate.as_view(),name='create'),
  url(r'^update/(?P<pk>\d+)/$',LectureUpdate.as_view(),name='update'),
  url(r'^search/$',LectureSearchList.as_view(),name='search'),
  url(r'^(?P<pk>\d+)/$',LectureDetail.as_view(),name='detail'),
]
