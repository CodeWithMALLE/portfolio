from django.db import models


# Create your models here.


class Clients(models.Model):

	options_profil = (
		("entreprise", "Entreprise"),
		("particulier", "Particulier")
	)

	last_name = models.CharField(max_length=50, verbose_name="Nom du client")
	first_name = models.CharField(max_length=50, verbose_name="Prénom du client")
	profil = models.CharField(max_length=50, verbose_name="Status du client", choices=options_profil)
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

