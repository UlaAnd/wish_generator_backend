import openai

from wish_generator.prod import api_key

openai.api_key = api_key  # type: ignore # noqa

class OpenAiController:
    def __init__(self) -> None:
        self.api_key = openai.api_key
        self.api_url = "https://api.openai.com/v1/"
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def get_completio2n(self, prompt: str) -> str:
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages, max_tokens=100, temperature=0.8
        )
        print(completion.choices[0].message["content"])
        return completion.choices[0].message["content"]

    def get_completion(self, prompt: str, system="You are a helpful assistant, your answer are no longer then 5 sentenses") -> str:
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ]
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        return completion.choices[0].message.content