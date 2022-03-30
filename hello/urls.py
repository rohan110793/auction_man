from django.urls import path, include
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signin", views.signIn, name="signin"),
    path("postsign/", views.postsign)
]
