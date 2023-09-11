from django.contrib import admin

from wishes.models import GeneratedWish, WishInformation


class WishInformationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "occasion",
        "wishes_format",
    ]


class GeneratedWishAdmin(admin.ModelAdmin):
    list_display = ["id", "wish_information", "text"]


admin.site.register(GeneratedWish, GeneratedWishAdmin)
admin.site.register(WishInformation, WishInformationAdmin)
