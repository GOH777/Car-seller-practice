from django.db import models

# Create your models here.

class Car(models.Model):
    """Модель для машин"""
    name = models.TextField('Название', max_length=40)
    model_name = models.TextField('Наименование модели', max_length=40)
    year = models.TextField('Год выпуска', max_length=4)
    country = models.TextField('Страна производитель', max_length=20)


    def __str__(self):
        """Функция для корректного вызова"""
        return f"Car: {self.name} {self.model_name}"
