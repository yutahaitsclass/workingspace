import django_filters
from rest_framework import viewsets, filters
from rest_framework import serializers
from myapp.models import Article, User
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'  
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields='__all__' 