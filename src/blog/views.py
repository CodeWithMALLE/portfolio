from django.shortcuts import render, redirect

from .models import Articles, Categories

# Create your views here.


def index(request):
	cats = Categories.objects.all()
	return render(request, "blog/index.html", {"cats": cats})


def publier_article(request):
	if request.user.is_authenticated:
		return render(request, "blog/publier_article.html")
	return redirect("accounts:login")
