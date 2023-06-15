from django import forms
from .models import Contact, CommanderService
from crispy_forms.bootstrap import StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ["first_name", "last_name", "email", "tel", "msg"]


class CommanderServiceForm(forms.ModelForm):
	class Meta:
		model = CommanderService
		fields = "__all__"
