from django.db import models

# Create your models here.
class Services(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name= "Название услуги"
    )
    description = models.TextField(
        verbose_name="Описание услуги"
    )
    desc = models.TextField(
        verbose_name="Описание для связи"
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'

class Projects(models.Model):
    num = models.IntegerField(
        verbose_name="Число завершенных пректов"
    )
    review = models.IntegerField(
        verbose_name="Число отзывов"
    )
    def __int__(self) -> str:
        return self.num 
    
    class Meta:
        verbose_name = 'Проекты'
        verbose_name_plural = 'Проекты'


class Education(models.Model):
    s = models.BigIntegerField(
        verbose_name= "С"
    )
    po = models.BigIntegerField(
        verbose_name="по"
    )
    name = models.CharField(
        max_length=255,
        verbose_name= "Место обучение"
    )
    desc = models.TextField(
        verbose_name="Описание"
    )
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Образвание'
        verbose_name_plural = 'Образвание'

class Skills(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Скилл"
    )
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Скиллы'
        verbose_name_plural = 'Скиллы'


class Parfolio(models.Model):
    image = models.ImageField(
        upload_to='photo/',
        verbose_name="ОПИСАНИЕ"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="название"
    )
    silka = models.URLField(
        verbose_name="Ссылка"
    )
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Последенее партфолио'
        verbose_name_plural = 'Последенее партфолио'


class Review(models.Model):
    image = models.ImageField(
        upload_to="photo/",
        verbose_name="Фото"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    dol = models.CharField(
        max_length=255,
        verbose_name="Должность"
    )
    desc = models.TextField(
        verbose_name="Описание"
    )
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Отзывы клиентов'
        verbose_name_plural = 'Отзывы клиентов'


class Blog(models.Model):
    image = models.ImageField(
        upload_to="photo/",
        verbose_name="фото"
    )
    data = models.DateField(
        auto_now_add = True,
        blank = True, null = True
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Навзание"
    )
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'
