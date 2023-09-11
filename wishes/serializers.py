from rest_framework import serializers

from wishes.models import GeneratedWish, WishInformation


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
