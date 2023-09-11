from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework import status
from rest_framework.response import Response

from wishes.models import GeneratedWish, WishInformation
from wishes.serializers import GeneratedWishSerializer
from wishes.services import WishGenerateService


@api_view(["POST"])
@csrf_exempt
def generate_wish(request: Request) -> HttpResponse:
    data = request.data
    wish_info = WishInformation.objects.create(
        name=data["name"],
        author_name=data["author_name"],
        occasion=data["occasion"],
        interests=data["interests"],
        style=data["style"],
        wishes_format=data["wishes_format"],
        connection_kind=data["connection_kind"],
    )
    controller = WishGenerateService()
    wish = controller.generate_wish(info=wish_info)
    wish_text_model = GeneratedWish.objects.create(
        wish_information=wish_info, text=wish
    )
    serializer = GeneratedWishSerializer(wish_text_model)
    return Response(serializer.data,  status=status.HTTP_201_CREATED)
