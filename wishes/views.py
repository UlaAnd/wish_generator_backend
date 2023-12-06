import requests
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework import status
from rest_framework.response import Response

from wishes.controllers import OpenAiController
from wishes.models import GeneratedWish, WishInformation, Question, Replay
from wishes.serializers import GeneratedWishSerializer, ReplaySerializer
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



@api_view(["POST"])
@csrf_exempt
def generate_replay(request: Request) -> HttpResponse:
    data = request.data
    question = data.get("question")
    Question.objects.create(text=question)
    all_questions = Question.objects.all()
    all_texts = [question.text for question in all_questions]
    system = f"Answer the question also with info below {all_texts}"
    controller = OpenAiController()
    replay = controller.get_completion(prompt=question, system=system)
    full_replay = {"reply": replay}

    return Response(full_replay,  status=status.HTTP_201_CREATED)


def send_question():
    url = 'https://wishgenerator.onrender.com/generate-replay/'  # Replace with your actual domain and port
    question_data = {
        'question': 'Your actual question goes here',
        # Include any other required data in the request body
    }
    response = requests.post(url, data=question_data)

    if response.status_code == 201:  # Assuming successful creation status
        reply_data = response.json()
        print("Generated Reply:", reply_data['text'])
    else:
        print("Error:", response.status_code, response.text)



