from django.contrib import admin
from tdlist.models import Tasklist

@admin.register(Tasklist)
class TasklistAdmin(admin.ModelAdmin):
    """Отображение модели Tasklist в админке."""

    list_display = (
        "id",
        "taskText",
        "created_time",
        "is_done",
        "finish_time",
    )
    readonly_fields = ["finish_time"]
    search_fields = ("id", "taskText")  # по каким полям будет производиться поиск