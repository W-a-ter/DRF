import re

from rest_framework.exceptions import ValidationError


class LessonVideoValidator:
    """Валидатор проверки видео в уроках, ссылка может быть только с youtube.com"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile("youtube.com")
        tep_val = dict(value).get(self.field)
        if not reg.search(tep_val):
            raise ValidationError("Video add only youtube.com")