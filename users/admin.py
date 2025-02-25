from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Отображает модели пользователей в админке"""

    list_display = (
        "id",
        "email",
    )
    list_filter = ("email",)
    search_fields = (
        "id",
        "email",
    )
