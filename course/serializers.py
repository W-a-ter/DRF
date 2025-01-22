from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from course.models import Course, Lesson, SubscriptionCourse
from course.validators import LessonVideoValidator


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
        validators = [LessonVideoValidator(field="video")]

    def get_lesson(self, obj):
        return obj.lesson.count()


class SubscriptionCourseSerializer(ModelSerializer):

    class Meta:
        model = SubscriptionCourse
        fields = "__all__"
