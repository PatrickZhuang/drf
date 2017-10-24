from rest_framework.routers import DefaultRouter

from quickstart.views import *

urlpatterns = [
    # APIView方法
    # url(r'^$', NewsListView.as_view()),
    # url(r'^(?P<pk>\d+)/$', NewsView.as_view()),

    # generic view 方式
    # url(r'^(?P<id>\d+)/$', NewsGenericView.as_view()),
    # url(r'^$', NewsListGenericView.as_view()),
]

# 使用view set方式
router = DefaultRouter()
# base_name可以为空，如果为空则DefaultRouter会根据viewSet的queryset属性来获取，queryset.model._meta.object_name.lower()
router.register('', NewsViewSet, base_name='news')
urlpatterns += router.urls
