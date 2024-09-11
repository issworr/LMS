from rest_framework.serializers import ModelSerializer
from .models import Author,Category,Book,User

class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields =['username','email','password']


class AuthorSerializers(ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name']

class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']     


class BookSerializers(ModelSerializer):
    author = AuthorSerializers()
    category = CategorySerializers()  

    class Meta:
        model = Book
        fields = ['id','title','author','category','file']         