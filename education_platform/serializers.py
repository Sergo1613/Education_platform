from rest_framework import serializers

from education_platform.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели курса"""

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для модели урока"""

    class Meta:
        model = Lesson
        fields = '__all__'
