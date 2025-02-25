from rest_framework.serializers import ModelSerializer, SerializerMethodField

from course.models import Course, Lesson, SubscriptionCourse
from course.validators import LessonVideoValidator


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [LessonVideoValidator(field='video')]


class SubscriptionCourseSerializer(ModelSerializer):

    class Meta:
        model = SubscriptionCourse
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)
    subscription = SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_lesson_count(self, obj):
        return obj.lesson.count()

    def get_subscription(self, obj):
        return True if SubscriptionCourse.objects.filter(user=self.context['request'].user, course=obj.pk) else False
