from django.utils.text import slugify
from portfolio.settings import AUTH_USER_MODEL
from django.db import models

# Create your models here.

User = AUTH_USER_MODEL


class Commentaires(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	content = models.TextField()

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name = "Commentaire"
		verbose_name_plural = "Les Commentaires"


class Categories(models.Model):
	nom = models.CharField(max_length=100, verbose_name="Nom de la catégorie")
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nom)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.nom

	class Meta:
		verbose_name = "Catégorie"
		verbose_name_plural = "Les Catégories"


class Articles(models.Model):
	titre = models.CharField(max_length=100, verbose_name="Titre")
	slug = models.SlugField(null=True)
	img = models.ImageField(
		upload_to="articles_pictures/", verbose_name="Image d'illustration"
		)
	content = models.TextField()
	date_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
	categorie = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name="Catégorie")
	commentaire = models.ManyToManyField(Commentaires, null=True, blank=True)
	auteur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.titre)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.titre

	class Meta:
		verbose_name = "Article"
		verbose_name_plural = "Les Articles"
