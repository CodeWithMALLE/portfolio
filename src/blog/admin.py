from django.contrib import admin

from .models import Articles, Categories, Commentaires


# Register your models here.


class ArticlesAdmin(admin.ModelAdmin):
	fields = ("auteur", "titre", "content", "img", "categorie", "commentaire")


class CategoriesAdmin(admin.ModelAdmin):
	fields = ("nom", )


class CommentairesAdmin(admin.ModelAdmin):
	fields = ('user', "content")


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Commentaires, CommentairesAdmin)

