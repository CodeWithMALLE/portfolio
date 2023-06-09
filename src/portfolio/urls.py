"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

app_name = "portfolio"
handler404 = "mysite.views.page_not_found_view"


# handler404 = 'myapp.views.page_not_found_view'


def seo(request):
    return render(request, "seo/google779eb3315ac6f149.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("mysite.urls"), name="site"),
    path('blog/', include("blog.urls"), name="blog"),
    path('accounts/', include("accounts.urls"), name="accounts"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
