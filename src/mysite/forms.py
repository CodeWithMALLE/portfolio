from django import forms
from .models import Contact, CommanderService


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ["first_name", "last_name", "email", "tel", "msg"]


class CommanderServiceForm(forms.ModelForm):
	class Meta:
		model = CommanderService
		fields = "__all__"
