from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from users.models import User
from users.serializers import UserRegistrationSerializer, UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """ Контроллер для регистрации пользователя """

    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()


class UserListAPIView(generics.ListAPIView):
    """ Контроллер для вывода списка пользователей"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ Контроллер для просмотра конкретного пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class UserUpdateAPIView(generics.UpdateAPIView):
    """ Контроллер для изменения пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class UserDestroyAPIView(generics.DestroyAPIView):
    """ Контроллер для удаления пользователя"""

    queryset = User.objects.all()
    permission_classes = [IsAdminUser]

