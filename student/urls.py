from django.conf.urls import url

from .views import StudentCreate, Login, Logout

urlpatterns = [
  url(r'^create/$',StudentCreate,name='create'),
  url(r'^login/$',Login,name='login'),
  url(r'^logout/$',Logout,name='logout'),
]
