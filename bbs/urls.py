from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from bbs import views

urlpatterns = [
    url(r'^$', views.BbsList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.BbsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)