from django.urls import path
from .views import index, a_propos, cv, services, projets, contact, commander_service

app_name = "mysite"

urlpatterns = [
    path("", index, name="index"),
    path("qui-suis-je/", a_propos, name="a_propos"),
    path("cv/", cv, name="cv"),
    path("services/", services, name="services"),
    path("projets/", projets, name="projets"),
    path("contact/", contact, name="contact"),
    path("commander-un-site/", commander_service, name="commander-service"),
]
