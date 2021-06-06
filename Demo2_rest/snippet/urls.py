from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SnippetList, SnippetDetail, SnippetList_mix, SnippetDetail_mix, UserDetail, UserList

urlpatterns = [
    re_path(r'^$', SnippetList_mix.as_view()),
    re_path(r'^(?P<pk>[0-9]+)/$', SnippetDetail_mix.as_view()),
    re_path(r'^users/$', UserList.as_view()),
    re_path(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

