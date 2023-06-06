from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import ArticleForm
from .models import Articles, Categories, Commentaires
from accounts.models import AccountsAuth


# Create your views here.


def index(request):
	cats = Categories.objects.all()
	articles = Articles.objects.all().order_by("-date_creation")
	return render(request, "blog/index.html", {"cats": cats, "articles": articles})


def publier_article(request):
	if request.user.is_authenticated:
		form = ArticleForm(request.FILES)
		user = request.user
		if request.method == "POST":
			form = ArticleForm(request.POST, request.FILES)
			if form.is_valid():
				article = form.save(commit=False)
				article.auteur = user
				article.save()
				return redirect("blog:index")
			return render(request, "blog/publier_article.html", {"form": form})
		return render(request, "blog/publier_article.html", {"form": form})

	return redirect("accounts:login_user")


def modifier_article(request, slug):
	if request.user.is_authenticated:
		user = request.user
		article = get_object_or_404(Articles, slug=slug)

		if request.POST:
			if article.auteur == user:
				form = ArticleForm(request.POST, instance=article)
				if form.is_valid():
					formm = form.save(commit=False)
					formm.auteur = user
					form.save(commit=True)
					return redirect("blog:index")
		form = ArticleForm(instance=article)
		return render(request, "blog/modifier_article.html", {"form": form})
	return redirect("accounts:login_user")


def detail_article(request, slug):
	article = get_object_or_404(Articles, slug=slug)
	comments = article.commentaire.all()
	auteur = article.auteur
	return render(
		request, "blog/detail-article.html", {
			"article": article, "comments": comments,
			"auteur": auteur
		}
		)


def commenter(request, slug):
	if request.method == "POST":
		content = request.POST["comment"]
		if content != "":
			user = request.user
			commentaire = Commentaires(content=content, user=user)
			commentaire.save()
			article = get_object_or_404(Articles, slug=slug)
			article.commentaire.add(commentaire)
			article.save()
	return redirect(reverse("blog:index"))
