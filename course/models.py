from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название', blank=True, null=True)
    picture = models.ImageField(verbose_name='Превью', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, verbose_name="владелец", null=True,
                              blank=True)
    amount = models.PositiveIntegerField(default=0, verbose_name="сумма покупки", blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название', blank=True, null=True)
    picture = models.ImageField(verbose_name='Превью', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    video = models.URLField(max_length=515, verbose_name='ссылка на видео', blank=True, null=True
                            )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lesson", verbose_name="курс", blank=True,
                               null=True)
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, verbose_name="владелец", null=True, blank=True)
    amount = models.PositiveIntegerField(default=0, verbose_name="сумма покупки", blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class SubscriptionCourse(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name="пользователь", blank=True,
                             null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс", blank=True, null=True)

    def __str__(self):
        return f"Подписка на курс #{self.course}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
