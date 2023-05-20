from django.urls import path
from .views import index, a_propos, cv

app_name = "mysite"

urlpatterns = [
    path("", index, name="index"),
    path("qui-suis-je/", a_propos, name="a_propos"),
    path("cv/", cv, name="cv")
]
