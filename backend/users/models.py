from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint


class User(AbstractUser):
    REQUIRED_FIELDS = (
        "username",
        "first_name",
        "last_name",
    )
    USERNAME_FIELD = "email"
    email = models.EmailField(
        verbose_name="Электронная почта",
        max_length=254,
        unique=True,
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        related_name="follow",
        verbose_name="Подписчик",
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        related_name="following",
        verbose_name="Автор",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"Автор: {self.author}, подписчик: {self.user}"

    class Meta:
        ordering = ["-id"]
        constraints = [
            UniqueConstraint(fields=["user", "author"], name="unique_follower")
        ]
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
