from django.urls import path
from . import views

# Даем название чтобы обратится по адресу "shop:single_course"
# из другово приложения
app_name = 'shop'
# <a href={% url "shop:single_course" course.id%}>{{ course.title }}</a>

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>', views.single_course, name='single_course'),
]
