from rest_framework import viewsets

from wishes.models import GeneratedWish, WishInformation
from wishes.serializers import GeneratedWishSerializer, WishInformationSerializer


class WishInformationViewSet(viewsets.ModelViewSet):
    queryset = WishInformation.objects.all()
    serializer_class = WishInformationSerializer


class GeneratedWishViewSet(viewsets.ModelViewSet):
    queryset = GeneratedWish.objects.all()
    serializer_class = GeneratedWishSerializer
