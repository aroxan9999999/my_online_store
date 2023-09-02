from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryView.as_view()),
    path('catalog/', views.CatalogView.as_view()),
    path('products/popular/', views.PopularProductsView.as_view()),
    path('products/limited/', views.LimitedProductListView.as_view()),
    path("sales/", views.SalesProductListView.as_view()),
    path('banners/', views.BannerViewSet.as_view()),
    path('product/<int:pk>/', views.ProductDetailView.as_view()),
    path('product/<int:pk>/review/', views.ProductReviewView.as_view()),
    path('tags/', views.TagListView.as_view()),
]