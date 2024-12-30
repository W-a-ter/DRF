from django.db import models


class Course(models.Model):
    title = models.CharField(verbose_name="Название")
    picture = models.ImageField(verbose_name="Превью", blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(verbose_name="Название")
    picture = models.ImageField(verbose_name="Превью", blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    video = models.URLField(verbose_name="ссылка на видео")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lesson", verbose_name="курс")
    owner = models.ForeignKey("users.User", on_delete=models.SET_NULL, verbose_name="владелец", null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
