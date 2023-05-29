from django.utils.text import slugify
from portfolio.settings import AUTH_USER_MODEL
from django.db import models

# Create your models here.

User = AUTH_USER_MODEL


class Categories(models.Model):
	nom = models.CharField(max_length=100, verbose_name="Nom de la catégorie")
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nom)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.nom


class Articles(models.Model):
	titre = models.CharField(max_length=100, verbose_name="Titre")
	slug = models.SlugField(null=True)
	date_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
	categorie = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name="Catégorie")

	def save(self, *args, **kwargs):
		self.slug = slugify(self.titre)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.titre
