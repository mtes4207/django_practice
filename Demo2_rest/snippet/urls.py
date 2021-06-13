from django.urls import re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SnippetList, SnippetDetail, SnippetList_mix, SnippetDetail_mix, UserDetail, UserList, SnippetHighlight
from .views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

json_urlpatterns = [
    re_path(r'^$', SnippetList_mix.as_view()),
    re_path(r'^(?P<pk>[0-9]+)/$', SnippetDetail_mix.as_view()),
    re_path(r'^users/$', UserList.as_view()),
    re_path(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
]
json_urlpatterns += [
    re_path(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

html_urlpatterns = [
    re_path(r'^$', api_root),
    re_path(r'^snippets/$',
        SnippetList_mix.as_view(),
        name='snippet-list'),
    re_path(r'^snippets/(?P<pk>[0-9]+)/$',
        SnippetDetail_mix.as_view(),
        name='snippet-detail'),
    re_path(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
        SnippetHighlight.as_view(),
        name='snippet-highlight'),
    re_path(r'^users/$',
        UserList.as_view(),
        name='user-list'),
    re_path(r'^users/(?P<pk>[0-9]+)/$',
        UserDetail.as_view(),
        name='user-detail')

]


######      View Set List      #######

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

view_set_urlpatterns = [
    re_path(r'^$', api_root),
    re_path(r'^snippets/$', snippet_list, name='snippet-list'),
    re_path(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
    re_path(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
    re_path(r'^users/$', user_list, name='user-list'),
    re_path(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
]

'''router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)

# API URL现在由路由器自动确定。
# 另外，我们还要包含可浏览的API的登录URL。
urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]'''

urlpatterns = format_suffix_patterns(view_set_urlpatterns)


