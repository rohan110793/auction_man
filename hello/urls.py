from django.urls import path, include
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signin", views.signIn, name="signin"),
    path("signup", views.signUp, name="signup"),
    path("postsign/", views.postsign),
    path("postsignup/", views.postsignup),
]
