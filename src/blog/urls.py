from django.urls import path
from .views import index, publier_article, detail_article, commenter


app_name = "blog"
urlpatterns = [
	path('', index, name="index"),
	path('publier-article/', publier_article, name="publier-article"),
	path('article/<slug:slug>/', detail_article, name="detail-article"),
	path('commentaire/<slug:slug>/', commenter, name="comment-article"),
]
