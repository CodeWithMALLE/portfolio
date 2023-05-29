from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class AccountsAuth(AbstractUser):
	class Meta:
		verbose_name = "Auteur de l'article"
		verbose_name_plural = "Les auteurs des articles"
