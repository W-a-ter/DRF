from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from course.models import Course, Lesson
from course.serializers import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    """Реализация представления создания уроков через generic. CreateAPIView"""

    serializer_class = CourseSerializer


class LessonListAPIView(generics.ListAPIView):
    """Реализация представления просмотра всех уроков через generic. ListAPIView"""

    serializer_class = CourseSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Реализация представления просмотра одного урока через generic. ListAPIView"""

    serializer_class = CourseSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Реализация представления изменения урока через generic. UpdateAPIView"""

    serializer_class = CourseSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Реализация представления удаления урока через generic. DestroyAPIView"""

    queryset = Lesson.objects.all()
