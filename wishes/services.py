from .controllers import OpenAiController
from .models import WishInformation


class WishGenerateService:
    def __init__(self) -> None:
        self.controller = OpenAiController()

    def generate_wish(self, info: WishInformation) -> str:
        prompt = self.get_prompt(info)
        completion = self.controller.get_completion(prompt=prompt)
        return completion

    def get_prompt(self, info: WishInformation) -> str:
        prompt = f"""
            Make original wishes:
            - language: Polish,
            - occasion: {info.occasion},
            - wish style: {info.occasion},
            - wishes_format: "rhyming, every 2 lines should have the same number of syllables",
            - for : {info.connection_kind},
            - name: {info.name},
            - from: {info.author_name},
            - length of 5 sentences,
            - you can mention: {info.interests},
            """
        return prompt

    def get_format(self, chosen_format: str) -> str:
        if chosen_format == WishInformation.FORMAT_GREETING:
            return "normal greetings"
        elif chosen_format == WishInformation.FORMAT_JOKE:
            return "wishes in the form of a joke"
        else:
            return "rhyming, every 2 lines should have the same number of syllables"

