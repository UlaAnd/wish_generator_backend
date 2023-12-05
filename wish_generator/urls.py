"""wish_generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from wishes.api import GeneratedWishViewSet, WishInformationViewSet, ReplayViewSet, QuestionViewSet
from wishes.views import generate_wish, generate_replay

router_wishes = routers.DefaultRouter()
router_wishes.register(r"wishes-informations", WishInformationViewSet)
router_wishes.register(r"wish-text", GeneratedWishViewSet)
router_wishes.register(r"question", QuestionViewSet)
router_wishes.register(r"replay", ReplayViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v2/", include(router_wishes.urls)),
    path("generate-wish", generate_wish, name="generate_wish"),
    path("generate-replay/", generate_replay, name="generate_replay"),

]
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
