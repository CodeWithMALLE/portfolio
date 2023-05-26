from django.contrib import admin
from .models import Projects, Clients, Contact


# from django.contrib.admin.templates import admin

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
	list_display = ("last_name", "first_name", "tel", "msg")
	list_filter = ("tel", "last_name")
	search_fields = ["tel", "last_name"]

	fieldsets = (
		("Nom", {
			"fields": ("first_name", "last_name"),
		}),
		("Contats", {
			"fields": ("tel", "email"),
		}),
		("Messages", {
			"fields": ('msg', ),
		}),
	)


class ClientsAdmin(admin.ModelAdmin):
	search_fields = ("last_name", "first_name")
	list_filter = ("last_name", "last_name")
	list_display = ('last_name', "first_name", 'profil', "tel")

	fieldsets = (
		("Nom clients", {
			"fields": ("first_name", "last_name")
		}),
		("Contacts client", {
			"fields": ("tel", "email"),
		}),
		("Type", {
			"fields": ("profil",),
		})
	)


class PrjectsAdmin(admin.ModelAdmin):
	list_display = ("name", "get_describes", "date")
	search_fields = ["name"]
	list_filter = ("name", "date")
	fieldsets = (
		("Nom du projet", {
			"fields": ("name",)
		}),
		("A propos du projet", {
			"fields": ("describes", "img"),
		}),
		(
			"Le client", {
				"fields": ("client",),
			}
		)
	)

	def get_describes(self, obj: Projects) -> str:
		return obj.describes[:20] + "..." if len(obj.describes) > 20 else obj.describes

	get_describes.short_description = "Description"


admin.site.register(Projects, PrjectsAdmin)
admin.site.register(Clients, ClientsAdmin)
admin.site.register(Contact, ContactAdmin)
