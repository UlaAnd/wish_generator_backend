from rest_framework import viewsets

from wishes.models import GeneratedWish, WishInformation, Question, Replay
from wishes.serializers import GeneratedWishSerializer, WishInformationSerializer, QuestionSerializer, ReplaySerializer


class WishInformationViewSet(viewsets.ModelViewSet):
    queryset = WishInformation.objects.all()
    serializer_class = WishInformationSerializer


class GeneratedWishViewSet(viewsets.ModelViewSet):
    queryset = GeneratedWish.objects.all()
    serializer_class = GeneratedWishSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ReplayViewSet(viewsets.ModelViewSet):
    queryset = Replay.objects.all()
    serializer_class =ReplaySerializer