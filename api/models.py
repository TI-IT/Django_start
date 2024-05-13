from tastypie.resources import ModelResource
from shop.models import Category, Course


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        # Разрешаем только меьод GET
        allowed_methods = ['get']


class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        # Разрешаем только меьод GET
        allowed_methods = ['get', 'post', 'delete']
