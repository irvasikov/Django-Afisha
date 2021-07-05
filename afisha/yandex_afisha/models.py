from django.db import models

class Places(models.Model):
    """Экскурсионные проекты"""
    title = models.CharField("Название", max_length=200)
    description_short = models.TextField("Краткое описание")
    description_long = models.TextField("Основной текст")
    lng = models.DecimalField("Долгота", max_digits=16, decimal_places=14)
    lat = models.DecimalField("Широта", max_digits=16, decimal_places=14)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Экскурсионный проект"
        verbose_name_plural = "Эксскурсионные проекты"

class Images(models.Model):
    """Изображения для экскурсионных проектов"""
    title = models.CharField("Название", max_length=200, default="Картинка")
    place = models.ForeignKey(Places, verbose_name="Экскурсионный проект", on_delete=models.CASCADE)
    image = models.ImageField("Изображение", upload_to='places/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

