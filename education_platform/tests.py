from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from education_platform.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        # Создание пользователя
        self.user = User.objects.create(
            email='test@gmail.com',
            password='testpassword',
            is_staff=True,
            is_active=True,
            is_superuser=True
        )

        self.course = Course.objects.create(
            name='test',
            description='first course'
        )

    def test_get_lesson_authenticated(self):
        """ Получение уроков авторизованным пользователем."""

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('education_platform:lesson-list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_lesson_create(self):
        """Тестирование для создания урока"""

        self.client.force_authenticate(user=self.user)

        data = {
            'name': 'test2',
            'description': 'this is second lesson',
            'video_link': 'https://youtube.com/123/',
            'course': self.course.id,
        }

        response = self.client.post(
            reverse('education_platform:lesson-create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Lesson.objects.all().count(),
            1
        )

    def test_lesson_update(self):
        """Тестирование обновления урока"""

        self.client.force_authenticate(user=self.user)

        self.lesson = Lesson.objects.create(
            name='test_lesson',
            description='first lesson',
            course=self.course,
        )

        updated_data = {
            'name': 'updated_lesson',
            'description': 'this is updated lesson',
            'course': self.course.id
        }

        response = self.client.put(
            reverse('education_platform:lesson-update', args=[self.lesson.id]),
            data=updated_data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.lesson.refresh_from_db()
        self.assertEqual(
            self.lesson.name,
            updated_data['name']
        )

        self.lesson.refresh_from_db()
        self.assertEqual(
            self.lesson.description,
            updated_data['description']
        )

    def test_delete_lesson(self):
        """Тестирование удаления урока"""

        self.client.force_authenticate(user=self.user)

        self.lesson = Lesson.objects.create(
            name='lesson_to_delete',
            description='lesson_to_delete description',
            course=self.course,
        )

        response = self.client.delete(
            reverse('education_platform:lesson-delete', args=[self.lesson.id]),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        # Убеждаемся, что урок удалён
        with self.assertRaises(Lesson.DoesNotExist):
            self.lesson.refresh_from_db()

