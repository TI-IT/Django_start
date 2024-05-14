from django.contrib import admin
from .models import Category, Course


# Какие поля видны в таблице всех курсов
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')


class CoursesInLine(admin.TabularInline):
    model = Course
    # Скрываем поле Дата создания created_at
    exclude = ['created_at']
    # Количество пустых полей для создания новых курсов
    extra = 1

# Какие поля видны на странице всех категорий


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    # Какие поля видны на странице одной категории
    fieldsets = [
        (None, {"fields": ['title']}),
        ('Дата', {
            "fields": ['created_at'],
            'classes': ['collapse'],
        }),
    ]
    # Добавляем информацию о курсах
    inlines = [CoursesInLine]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
