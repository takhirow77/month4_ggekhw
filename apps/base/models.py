from django.db import models

# Create your models here.
class Settings(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    image = models.ImageField(
        upload_to='photo/',
        verbose_name="Фотография"
    )
    job = models.CharField(
        max_length=255,
        verbose_name="Профессия"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    address = models.CharField(
        verbose_name="Адресс",
        max_length=255
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Номер телефона"
    )
    mail = models.CharField(
        max_length=255,
        verbose_name="Почта"
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Основная настройка'
        verbose_name_plural = 'Основные настройки'


