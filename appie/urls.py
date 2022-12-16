from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("articleView/<int:articleId>", views.articleView, name="articleView"),
    path("PostComment", views.PostComment, name="comment"),
    path("articlehub", views.articlehub, name="articlehub"),
    path("GivemeComment/<int:articleId>", views.comment, name="getcomment"),
]