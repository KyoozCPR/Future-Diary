from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("character/<int:id>/",views.character, name="character"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_func, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('user-profile', views.user_profile, name="user-profile"),
    path('user/<str:pk>', views.search_user, name='userquery')
]