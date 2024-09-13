from django.urls import path
from .views import HomeView, ArticleDetailView, ContactView, CategoryArticlesListView

urlpatterns = [
    path('', HomeView.as_view(), name="index"),
    path('article/<str:slug>/', ArticleDetailView.as_view(), name="detail"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('category/<slug:slug>/', CategoryArticlesListView.as_view(), name="category_articles"),
]