from django.core.validators import RegexValidator
from django.db import models
from django_countries.fields import CountryField


# Create your models here.


class Clients(models.Model):

	options_profil = (
		("entreprise", "Entreprise"),
		("particulier", "Particulier")
	)

	last_name = models.CharField(max_length=50, verbose_name="Nom du client")
	first_name = models.CharField(max_length=50, verbose_name="Prénom du client")
	profil = models.CharField(
		max_length=50, verbose_name="Status du client", choices=options_profil
	)
	tel = models.CharField(max_length=50, verbose_name='Numéro de télephone')
	email = models.EmailField(verbose_name="Adresse mail du client")

	class Meta:
		verbose_name = "Client"
		verbose_name_plural = "Les Clients"
		ordering = ["last_name"]


class Projects(models.Model):
	name = models.CharField(max_length=100, verbose_name="Projets", )
	img = models.ImageField(upload_to="mysite/project_img/")
	describes = models.TextField(verbose_name="Description du projet")
	date = models.DateField(auto_now_add=True, auto_now=False)
	client = models.ForeignKey(Clients, on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Projet"
		verbose_name_plural = "Les Projets"


class Contact(models.Model):
	first_name = models.CharField(max_length=50, verbose_name="Prénom")
	last_name = models.CharField(max_length=50, verbose_name="Nom de famille")
	email = models.EmailField(verbose_name="Adresse mail")
	tel = models.CharField(verbose_name="Numéro de téléphone", max_length=50)
	msg = models.TextField()

	def __str__(self):
		return f"Message de {self.last_name}"

	class Meta:
		verbose_name = "Contact"
		verbose_name_plural = "Les Contacts"


class CommanderService(models.Model):

	# Informations clients

	nom_entreprise = models.CharField(max_length=200)
	raison_social = models.CharField(max_length=300)
	domaine_dactivite = models.CharField(max_length=200)
	adresse = CountryField()
	ville = models.CharField(max_length=200)

	# Personne à conatacter en charge du projet

	nom_personne = models.CharField(max_length=200)
	prenom_personne = models.CharField(max_length=200)

	regexTel = r'^(+){1}\d{2,4}\s?\d{4,10}$'
	tel = models.CharField(
		max_length=100, validators=[RegexValidator(
			regex=regexTel,
			message="Ce n'est pas un serieux numéro de télephone !"
			)]
		)
	email = models.EmailField()

	# Informations du projet
	options_forme_projet = (
		("creation_de_site", "Création de site"),
		("refonte_du_site", "Refonte de site"),
		("amelioration_du_site", "Amélioration du site"),
	)
	forme_du_projet = models.CharField(max_length=100, choices=options_forme_projet)
	refonte_true = models.URLField(blank=True)

	# objectifs du site
	options_nature_projet = (
		("site_vitrine", "Site vitrine"),
		("site_ecommerce", "Refonte de site"),
		("portail_info", "Amélioration du site"),
	)
	nature_du_projet = models.CharField(max_length=100, choices=options_nature_projet)


