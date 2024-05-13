from tastypie.resources import ModelResource
from shop.models import Category, Course
from tastypie.authorization import Authorization
from .authentication import CustomAutentication


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
        # Разрешаем только меьод get,post,delete
        allowed_methods = ['get', 'post', 'delete']
        authentication = CustomAutentication()
        authorization = Authorization()

    """
        Дегидратирует переданный объект `bundle`, добавляя поле `category_id` в его словарь `data`.
        Аргументы:
            bundle (tastypie.bundle.Bundle): Объект, который нужно дегидратировать.
        Возвращает:
            tastypie.bundle.Bundle: Дегидратированный объект.
    """

    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        return bundle

    # Добавляем поле `category_id` в объект
    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category
        return bundle
