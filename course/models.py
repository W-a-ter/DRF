from django.db import models


class Course(models.Model):
    title = models.CharField(verbose_name="Название", null=True, blank=True)
    picture = models.ImageField(verbose_name="Превью", blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(verbose_name="Название", null=True, blank=True)
    picture = models.ImageField(verbose_name="Превью", blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    video = models.URLField(verbose_name="ссылка на видео", null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lesson", verbose_name="курс",
                               null=True, blank=True)
    owner = models.ForeignKey("users.User", on_delete=models.SET_NULL, verbose_name="владелец", null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class SubscriptionCourse(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name="пользователь",
                             null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс", null=True, blank=True)

    def __str__(self):
        return f"Подписка на курс #{self.course}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
