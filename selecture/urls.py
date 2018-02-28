"""selecture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import homepage
from lecture import urls as lecture_url
from student import urls as student_url
from timetable import urls as timetable_url
from review import urls as review_url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',homepage,name='homepage'),
    url(r'^admin/', admin.site.urls),
    url(r'^lecture/',include(lecture_url,namespace='lecture')),
    url(r'^student/',include(student_url,namespace='student')),
    url(r'^timetable/',include(timetable_url,namespace='timetable')),
    url(r'^review/',include(review_url,namespace='review')),
]

# urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
