
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Articles, Categories, Commentaires
from accounts.models import AccountsAuth


# Create your views here.


def index(request):
	cats = Categories.objects.all()
	articles = Articles.objects.all().order_by("-date_creation")
	return render(request, "blog/index.html", {"cats": cats, "articles": articles})


def publier_article(request):
	if request.user.is_authenticated:
		return render(request, "blog/publier_article.html")
	return redirect("accounts:login_user")


def detail_article(request, slug):
	article = get_object_or_404(Articles, slug=slug)
	comments = article.commentaire.all()
	return render(request, "blog/detail-article.html", {"article": article, "comments": comments})


def commenter(request, slug):
	if request.method == "POST":
		content = request.POST["comment"]
		if content != "":
			if request.user.is_authenticated:
				user = request.user
				commentaire = Commentaires(content=content, user=user)
			else:
				user = AccountsAuth.objects.create_user(
					"Non identifié", "Non identifié"
					)
				commentaire = Commentaires(content=content, user=user)
			commentaire.save()
			article = get_object_or_404(Articles, slug=slug)
			article.commentaire.add(commentaire)
			article.save()
	return redirect(reverse("blog:index"))

