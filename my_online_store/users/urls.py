from django.urls import path
from . import views

urlpatterns = [
    path('sign-in/', views.SignInView.as_view()),
    path('sign-up/', views.SignUpView.as_view()),
    path('sign-out/', views.SignOutView.as_view()),
    path('profile/', views.UserProfileView.as_view()),
    path('profile/password/', views.UserPasswordUpdateView.as_view()),
    path('profile/avatar/', views.UserAvatarUpdateView.as_view()),
]
