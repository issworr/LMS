from django.shortcuts import render 
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Author,Category,Book,User
from .serializers import AuthorSerializers, CategorySerializers,BookSerializers,UserSerializers



class UserApiView(ModelViewSet):
    queryset = User.objects.all()
    serializers_class = UserSerializers

    
class AuthorApiView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers




class CategoryApiView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class BookApiView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

def index(request):
    return render(request, 'templates/index.html')
