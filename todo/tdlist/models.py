from django.db import models
from datetime import datetime


class Tasklist(models.Model):
    """Список заданий"""

    taskText = models.CharField(
        max_length=200, help_text="Описание задачи", verbose_name="Текст задачи"
    )
    created_time = models.DateTimeField(
        default=datetime.now(), help_text="Дата создения задачи", verbose_name="Создано"
    )
    is_done = models.BooleanField(
        default=False, help_text="Пометка о выполнении", verbose_name="Выполнено"
    )
    finish_time = models.DateTimeField(
        default=None,
        help_text="Время завершения задачи",
        blank=True,
        null=True,
        verbose_name="Время завершения",
    )

    def save(self, *args, **kwargs) -> None:
        """Переопределение сохранения.

        Убирается или проставляется дата завершения, в зависимости от наличия признака завершения.
        """
        if self.is_done is False:
            self.finish_time = None
        else:
            if self.finish_time is None:
                self.finish_time = datetime.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        """Переопределение строкового представления объекта."""
        return f"Item {self.id}|{self.taskText}"
