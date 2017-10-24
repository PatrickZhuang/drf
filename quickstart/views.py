# Create your views here.
from rest_framework import views, status, generics, viewsets
from rest_framework.response import Response

from quickstart import serializers
from quickstart.models import News


# views.APIView 通过实现 (get、post、put、delete)方法来处理相应的rest method请求，通过覆盖一些policies属性来改变或者提供鉴权、权限、限流等功能
class NewsView(views.APIView):
    def get(self, request, pk):
        news = News.objects.get(pk=pk)
        return Response(news.title)

    def delete(self, request, pk):
        news = News.objects.get(pk=pk)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NewsListView(views.APIView):
    def get(self, request, *args, **kwargs):
        objects = [news.title for news in News.objects.all()]
        return Response(objects)

    def post(self, request, *args, **kwargs):
        title = request.data.get('title', '')
        content = request.data.get('content', '')
        news = News.objects.create(title=title, content=content)
        return Response(news)


# generic views
class NewsGenericView(generics.RetrieveUpdateDestroyAPIView):
    # 对应urlpatterns中的id，默认是pk，如果url中写的不是pk，则lookup_field值也要相应修改
    lookup_field = 'id'
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer


class NewsListGenericView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer


# view sets
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer
    # 可以用于控制可以接受的http方法
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
