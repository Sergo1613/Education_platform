from django.urls import path

from education_platform.apps import EducationPlatformConfig
from education_platform.views import CourseCreateAPIView, CourseListAPIView, CourseRetrieveAPIView, CourseUpdateAPIView, \
    CourseDestroyAPIView, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView

app_name = EducationPlatformConfig.name

urlpatterns = [
    path('course/create/', CourseCreateAPIView.as_view(), name='course-create'),
    path('course/', CourseListAPIView.as_view(), name='course-list'),
    path('course/<int:pk>/', CourseRetrieveAPIView.as_view(), name='course-get'),
    path('course/update/<int:pk>/', CourseUpdateAPIView.as_view(), name='course-update'),
    path('course/delete/<int:pk>/', CourseDestroyAPIView.as_view(), name='course-delete'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete')
]