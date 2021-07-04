from django.db import models

class Places(models.Model):
    title = models.CharField("Название", max_length=200)
    description_short = models.TextField("Краткое описание")
    description_long = models.TextField("Основной текст")
    lng = models.DecimalField("Долгота", max_digits=16, decimal_places=14)
    lat = models.DecimalField("Широта", max_digits=16, decimal_places=14)

