from django.db import models


class WishInformation(models.Model):
    STYLE_OFFICIAL = "official"
    STYLE_FUN = "fun"
    STYLE_FRIENDLY = "friendly"
    STYLE_INFORMAL = "informal"
    STYLE_CHOICES = (
        (STYLE_OFFICIAL, "official"),
        (STYLE_FUN, "fun"),
        (STYLE_FRIENDLY, "friendly"),
        (STYLE_INFORMAL, "informal"),
    )
    FORMAT_GREETING = "greeting"
    FORMAT_POEM = "poem"
    FORMAT_JOKE = "joke"
    FORMAT_CHOICES = (
        (FORMAT_GREETING, "greeting"),
        (FORMAT_POEM, "poem"),
        (FORMAT_JOKE, "joke"),
    )
    name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    occasion = models.CharField(max_length=255)
    interests = models.CharField(max_length=255)
    style = models.CharField(max_length=50, choices=STYLE_CHOICES)
    wishes_format = models.CharField(max_length=50, choices=FORMAT_CHOICES)
    connection_kind = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class GeneratedWish(models.Model):
    wish_information = models.ForeignKey(
        "wishes.WishInformation",
        on_delete=models.CASCADE,
    )
    text = models.TextField()
