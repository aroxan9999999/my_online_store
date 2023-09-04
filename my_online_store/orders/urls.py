from django.urls import path
from . import views


urlpatterns = [
    path('orders/', views.OrderView.as_view()),
    path('order/<int:pk>/', views.OrderDetailView.as_view()),
    path('basket/', views.BasketView.as_view()),
    path('payment/', views.PaymentView.as_view())
]