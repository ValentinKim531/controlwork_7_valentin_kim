from django.db import models
from django.db.models import TextChoices


# Create your models here.

class StatusChoice(TextChoices):
    ACTIVE = 'active', 'Активно'
    BLOCKED = 'blocked', 'Заблокировано'


class Guestbook(models.Model):
    author_name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Имя")
    mail = models.EmailField(max_length=50, null=False, blank=False, verbose_name="Электронная почта")
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")
    status = models.CharField(verbose_name='Статус', choices=StatusChoice.choices, max_length=20,
                              default=StatusChoice.ACTIVE, null=False, blank=False)

    def __str__(self):
        return f"{self.author_name} - {self.mail} - {self.text} - {self.status}"

    class Meta:
        verbose_name = "Записи"
        verbose_name_plural = "Гостевая книга"

