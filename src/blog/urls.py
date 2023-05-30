from django.urls import path
from .views import index, publier_article


app_name = "blog"
urlpatterns = [
	path('', index, name="index"),
	path('publier-article/', publier_article, name="publier-article"),
]
