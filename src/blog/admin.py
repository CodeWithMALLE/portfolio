from django.contrib import admin

from .models import Articles, Categories


# Register your models here.


class ArticlesAdmin(admin.ModelAdmin):
	fields = ("titre", "categorie")


class CategoriesAdmin(admin.ModelAdmin):
	fields = ("nom", )


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Categories, CategoriesAdmin)

