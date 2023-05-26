from django.shortcuts import render, redirect
from .models import Projects, Clients, Contact
from .forms import ContactForm
import os


# Create your views here.


def index(request):
	return render(request, "mysite/index.html")


def a_propos(request):
	return render(request, 'mysite/a-propos.html')


def cv(request):
	dev = {
		"HTML/CSS/JS": 80,
		"python": 70,
		"django": 50,
		"Bootstrap": 50,
		"sql/sqlite/mysql": 40,
	}
	mod = {
		"merise": 70,
		"uml": 50
	}
	ver = {
		"git/github": 45,
	}

	return render(request, "mysite/cv.html", context={"dev": dev, "mod": mod, "ver": ver})


def services(request):
	base = "/media/mysite/services-pictures/"
	cartes = {
		"Création de sites web": (
			base + "web-site.png",
			"Nous concevons et développons des "
			"sites web professionnels et "
			"modernes  quirépondent aux besoins "
			"uniques  de nos clients.<br><br>Nos "
			"sites web sont conçus pour offrir une"
			"expérience utilisateur exceptionnelle"
			"et une navigation fluide."
		),
		"Applications web et mobiles sur mesure": (
			base + "app.png",
			"Applications web et mobiles sur mesure Nous développons des applications web et "
			"mobiles personnalisées qui répondent aux exigences spécifiques de votre entreprise. "
			"<br><br>Nos applications sont conçues pour fonctionner de manière transparente sur "
			"différentes plateformes et offrir une convivialité optimale."
		),
		"Référencement de site": (
			base + "seo.png",
			"Nous optimisons votre site web pour les moteurs de recherche afin d'augmenter sa "
			"visibilité en ligne. <br><br>Grâce à nos techniques de référencement avancées, "
			"nous vous aidons à attirer un trafic qualifié et à améliorer votre classement dans les "
			"résultats de recherche."
		),
		"Intégration et création d'applications desktop": (
			base + "app-desk.png",
			"Nous offrons des services d'intégration et de développement d'applications desktop "
			"puissantes et fonctionnelles. <br><br>Que ce soit pour automatiser des processus "
			"métier "
			"ou "
			"pour améliorer l'efficacité opérationnelle, nous sommes là pour vous aider."
		),
		"Conception de bases de données": (
			base + "db.png",
			"Nous concevons des bases de données robustes et sécurisées pour stocker et gérer "
			"efficacement vos données. <br><br>Notre expertise en conception de bases de données vous "
			"assure une gestion efficace de vos informations critiques."
		),
		"Refonte de l'existant": (
			base + "refonte-site.png",
			"Nous améliorons les aspects visuels de votre site ou d'application déjà existant(e)."
			"<br>En plus nous ajoutons de nouvelles fonctionnalités ou "
			"des améliorations techniques, telles que l'intégration de médias sociaux, l'ajout de "
			"fonctionnalités de commerce électronique, l'intégration d'un blog."
		)
	}

	return render(request, "mysite/services.html", context={"cards": cartes, })


def projets(request):
	list_projet = Projects.objects.all()
	return render(request, "mysite/projects.html", context={"projets": list_projet})


def contact(request):
	template = ""
	form = ContactForm()

	if len(request.POST) > 0:
		form = ContactForm(request.POST)

		if form.is_valid():
			form.fisrt_name = request.POST["first_name"]
			form.last_name = request.POST["last_name"]
			form.email = request.POST["email"]
			form.tel = request.POST["tel"]
			form.msg = request.POST["msg"]

			form.save()
			template = "mysite/index.html"
			return redirect("mysite:index")
		else:
			template = "mysite/contact.html"
			return render(request, template)
	else:
		template = "mysite/contact.html"
		context = {}
		return render(request, template, context)
