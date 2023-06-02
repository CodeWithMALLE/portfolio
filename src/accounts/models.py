from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class AccountsAuth(AbstractUser):
	first_name = models.CharField(max_length=150, blank=False)
	last_name = models.CharField(blank=False, max_length=150)
	username = models.CharField(blank=False, max_length=150, unique=True)
	email = models.EmailField(blank=False, unique=True)

	class Meta:
		verbose_name = "Auteur de l'article"
		verbose_name_plural = "Les auteurs des articles"
