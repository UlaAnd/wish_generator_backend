import pytest

from wishes.controllers import OpenAiController
from wishes.models import WishInformation
from wishes.services import WishGenerateService
from wishes.views import generate_wish, send_question


@pytest.mark.django_db(True)
class TestWishGenerator:

    def test_creating_model_create_wish(self):
        info = WishInformation.objects.create(
            name="Asia",
            author_name="Ula",
            occasion="wedding",
            interests="music",
            style=WishInformation.STYLE_FRIENDLY,
            wishes_format=WishInformation.FORMAT_POEM,
            connection_kind="brother",
        )
        self.controller = WishGenerateService()
        wish = self.controller.generate_wish(info=info)
        assert wish is not None

    def test_ai(self):
        answer = send_question()
        return answer

    def test_ai(self):
        controller = OpenAiController()
        replay = controller.get_completion(prompt="question")
        return replay