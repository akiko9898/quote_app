from django.db import models
from django.core.exceptions import ValidationError

class Quote(models.Model):
    text = models.TextField(unique=True, verbose_name="Текст цитаты")
    author = models.CharField(max_length=200, verbose_name="Автор")
    source = models.CharField(max_length=200, verbose_name="Источник (фильм/книга)", blank=True)
    weight = models.PositiveIntegerField(default=1, verbose_name="Вес")
    views = models.PositiveIntegerField(default=0, verbose_name="Просмотры")
    likes = models.PositiveIntegerField(default=0, verbose_name="Лайки")
    dislikes = models.PositiveIntegerField(default=0, verbose_name="Дизлайки")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.author}: {self.text[:50]}"

    def clean(self):
        # Проверка дубликатов (unique=True на text уже обрабатывает, но для ясности)
        if Quote.objects.filter(text=self.text).exists():
            raise ValidationError("Цитата с таким текстом уже существует.")
        # Проверка лимита на источник
        if self.source:
            count = Quote.objects.filter(source=self.source).exclude(id=self.id).count()
            if count >= 3:
                raise ValidationError("Максимум 3 цитаты от одного источника.")