from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from course.models import Lesson, Course


class CourseSerializer(ModelSerializer):
    class Meta:
        class Meta:
            model = Course
            fields = "__all__"


class LessonSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()
    lesson = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = "__all__"

    def get_lesson_count(self, obj):
        return obj.lesson.count()