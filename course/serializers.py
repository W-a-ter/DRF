from rest_framework.serializers import ModelSerializer

from course.models import Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        class Meta:
            model = Lesson
            fields = "__all__"
