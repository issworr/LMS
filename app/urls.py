from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorApiView,CategoryApiView,BookApiView


router = DefaultRouter()
router.register(r'authors', AuthorApiView)
router.register(r'categories', CategoryApiView)
router.register(r'books', BookApiView)
urlpatterns = [
   
    path('author/',AuthorApiView.as_view({'get':'list','post':'create'})),
    path('category/',CategoryApiView.as_view({'get':'list','post':'create'})),
    path('book/',BookApiView.as_view({'get':'list','post':'create'})),

]
