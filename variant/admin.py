from django.contrib import admin

from .models import VariantOlympiad, Category, QuestionAnswerOlympiad, UserResultOlympiad


@admin.register(VariantOlympiad)
class VariantAdmin(admin.ModelAdmin):
    list_display = ['category', ]
    search_fields = ['category',]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name',]


@admin.register(UserResultOlympiad)
class UserResultOlympiadAdmin(admin.ModelAdmin):
    list_display = ['user', 'correct_answer', 'option']
    search_fields = ['user', 'option']
    readonly_fields = ('time_start_olympiad', 'end_start_olympiad')


@admin.register(QuestionAnswerOlympiad)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'question', 'answer']
    search_fields = ['category', 'question', ]
