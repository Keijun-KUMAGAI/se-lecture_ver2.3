from django.conf.urls import url
from .views import DeleteReview, UpdateReview

urlpatterns = [
    url(r'^delete/(?P<pk>\d+)/$',DeleteReview.as_view(),name='delete'),
    url(r'^update/(?P<pk>\d+)/$',UpdateReview.as_view(),name='update'),
]
