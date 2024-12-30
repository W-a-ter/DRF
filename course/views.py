from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from course.models import Course, Lesson
from course.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    """Реализация представления курсов через ViewSet (полный crud)"""

    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [~IsModerator]
        elif self.action in ["retrieve", "update"]:
            self.permission_classes = (IsModerator | IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (~IsModerator | IsOwner,)
        return super().get_permissions()


class LessonCreateAPIView(generics.CreateAPIView):
    """Реализация представления создания уроков через generic. CreateAPIView"""

    serializer_class = LessonSerializer
    permission_classes = (~IsModerator, IsAuthenticated)


class LessonListAPIView(generics.ListAPIView):
    """Реализация представления просмотра всех уроков через generic. ListAPIView"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Реализация представления просмотра одного урока через generic. ListAPIView"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsModerator | IsOwner,
    )


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Реализация представления изменения урока через generic. UpdateAPIView"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsModerator | IsOwner,
    )


class LessonDestroyAPIView(generics.DestroyAPIView):

    queryset = Lesson.objects.all()
    permission_classes = (
        IsAuthenticated,
        ~IsModerator | IsOwner,
    )
