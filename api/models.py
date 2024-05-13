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

        # Поля для исключения в ресурсе для клиента
        excludes = ['reviews_qty', 'created_at']

        authentication = CustomAutentication()
        authorization = Authorization()

# hydrate-обрабатываем данные от клиента к серверу
    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        return bundle

# dehydrate-обрабатываем данные от сервера к клиенту
    # Добавляем поле `category_id`, `category` в объект
    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category_id
        bundle.data['category'] = bundle.obj.category
        return bundle

    # Вносим изменения в Заголовок
    def dehydrate_title(self, bundle):
        return bundle.data['title'].upper()
