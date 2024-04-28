from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from education_platform.models import Course, Lesson
from education_platform.paginators import MyPaginator
from education_platform.serializers import CourseSerializer, LessonSerializer


class CourseCreateAPIView(generics.CreateAPIView):
    """ Контроллер для создания курса """

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAdminUser]


class CourseListAPIView(generics.ListAPIView):
    """ Контроллер для вывода списка курсов """

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MyPaginator


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    """ Контроллер для просмотра курса """

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]


class CourseUpdateAPIView(generics.UpdateAPIView):
    """ Контроллер для изменения курса """

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAdminUser]


class CourseDestroyAPIView(generics.DestroyAPIView):
    """ Контроллер для удаления курса """

    queryset = Course.objects.all()
    permission_classes = [IsAdminUser]


class LessonCreateAPIView(generics.CreateAPIView):
    """ Контроллер для создания урока """

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAdminUser]


class LessonListAPIView(generics.ListAPIView):
    """ Контроллер для вывода списка уроков """

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MyPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """ Контроллер для просмотра урока """

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """ Контроллер для изменения урока """

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAdminUser]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """ Контроллер для удаления урока """

    queryset = Lesson.objects.all()
    permission_classes = [IsAdminUser]




