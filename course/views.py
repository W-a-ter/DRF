from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from course.models import Course, Lesson
from course.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend, SearchFilter]
    search_fields = ['payment_method']
    ordering_fields = ['date_pay']
    filterset_fields = ['lesson', 'course']


class LessonCreateAPIView(generics.CreateAPIView):
    """Реализация представления создания уроков через generic. CreateAPIView"""

    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    """Реализация представления просмотра всех уроков через generic. ListAPIView"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Реализация представления просмотра одного урока через generic. ListAPIView"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Реализация представления изменения урока через generic. UpdateAPIView"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):

    queryset = Lesson.objects.all()
