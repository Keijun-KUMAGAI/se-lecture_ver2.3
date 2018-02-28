from django.conf.urls import url
from .views import TimetableDetail,TimetableList,TimetableRegister,TimetableAnregister

urlpatterns = [
    url(r'^$',TimetableDetail.as_view(),name='detail'),
    url(r'^search/$',TimetableList.as_view(),name='search'),
    url(r'^register/$',TimetableRegister.as_view(),name='register'),
    url(r'^register/$',TimetableAnregister.as_view(),name='delete'),
]
