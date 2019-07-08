
from rest_framework import viewsets, routers
from myapp.models import Article
from myapp.serializers import ArticleSerializer
 
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
 
router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)