from django.conf.urls import include, url
from django.conf.urls import handler404, handler500

from word import views

urlpatterns = [
    url(r'^keywords/search', views.search, name='search'),
    url(r'^keywords', include('word.urls')),
]

handler404 = views.error_404
handler500 = views.error_500
