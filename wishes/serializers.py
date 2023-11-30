from rest_framework import serializers

from wishes.models import GeneratedWish, WishInformation, Question, Replay


class WishInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishInformation
        fields = (
            "id",
            "name",
            "occasion",
            "interests",
            "author_name",
            "wishes_format",
            "updated_at",
            "style",
            "connection_kind",
        )


class GeneratedWishSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneratedWish
        fields = (
            "id",
            "wish_information",
            "text",
        )


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            "id",
            "text",
        )


class ReplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Replay
        fields = (
            "id",
            "text",
        )

