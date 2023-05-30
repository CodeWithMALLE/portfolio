from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout

# Create your views here.

User = get_user_model()


def logout_user(request):
	logout(request)
	return redirect("blog:index")


def login_user(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]

		user = authenticate(username=username, password=password)

		if user:
			login(request, user=user)
			return redirect("blog:index")
		else:
			return render(request, "accounts/login.html", {"errors": "Identifiants non valide !"})
	return render(request, "accounts/login.html")


def signup(request):
	if request.POST:
		first_name = request.POST["first_name"]
		last_name = request.POST["last_name"]
		username = request.POST["username"]
		email = request.POST["email"]
		password = request.POST["password"]

		try:
			user = User.objects.create_user(
				username=username, last_name=last_name,
				first_name=first_name, email=email, password=password
				)
		except:
			errors = "Formulaire invlaide ! tous les champs sont obligatoires"
			return render(request, "accounts/signup.html", {"errors": errors})

		login(request, user=user)
		return redirect("blog:index")
	return render(request, "accounts/signup.html")

