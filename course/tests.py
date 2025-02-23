from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from course.models import Lesson, Course
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()

        self.user = User.objects.create(email="test@mail.ru", password="123qwe")
        self.course = Course.objects.create(title="test_course")
        self.lesson = Lesson.objects.create(
            title="test_lesson", video="https://test.youtube.com/", course=self.course, owner=self.user
        )

        self.client.force_authenticate(user=self.user)

    def test_getting_lesson_list(self):
        """Тестирование получения списка уроков."""
        response = self.client.get("/lesson/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json()["results"],
            [
                {
                    "id": 1,
                    "title": "test_lesson",
                    "picture": None,
                    "description": None,
                    "video": "https://test.youtube.com/",
                    "course": 1,
                    "owner": 1,
                }
            ],
        )

    def test_lesson_create(self):
        """Тестируем создание урока"""
        url = reverse("course:lesson-create")
        data = {"title": "test_lesson_1", "course": self.course.pk, "video": "https://youtube.com/"}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(
            response.json(),
            {
                "id": 3,
                "title": "test_lesson_1",
                "picture": None,
                "description": None,
                "video": "https://youtube.com/",
                "course": 2,
                "owner": 2,
            },
        )

    def test_lesson_update(self):
        """Тестируем изменение урока"""
        url = reverse("course:lesson-update", args=(self.lesson.pk,))
        data = {"title": "test_lesson_2", "video": "https://test.youtube.com/"}

        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json()["title"], "test_lesson_2")

    def test_lesson_detail(self):
        """Тестируем изменение урока"""
        url = reverse("course:lesson-detail", args=(self.lesson.pk,))

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json()["title"], "test_lesson")

    def test_lesson_delete(self):
        """Тестируем изменение урока"""
        url = reverse("course:lesson-delete", args=(self.lesson.pk,))

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Lesson.objects.all().count(), 0)
