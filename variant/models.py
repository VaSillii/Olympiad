from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


def validate_file_extension(value):
    if value.file.content_type != 'text/plain':
        raise ValidationError('The uploaded file must be a text file')


def content_file_name(user, filename):
    return "File-answer/{folder}/{filename}".format(folder=user.user.username, filename=filename)


class QuestionAnswerOlympiad(models.Model):
    PATH = 'Question-image/'

    question_img = models.ImageField(upload_to=PATH, blank=True, null=True, verbose_name='Изображения вопроса')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    question = models.CharField(max_length=300, verbose_name='Вопрос')
    answer = models.CharField(max_length=300, verbose_name='Ответ')

    def get_img(self):
        if not self.question_img:
            return ''
        return self.question_img.url

    def img_tag(self):
        if self.question_img:
            return mark_safe('<img src="%s" class="mg-fluid img-thumbnail" />' % self.get_img())
        return ''

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Вопрос и ответ"
        verbose_name_plural = "Вопросы и ответы"


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class VariantOlympiad(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    questions = models.ManyToManyField(QuestionAnswerOlympiad, verbose_name='Вопросы варианта')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Вариант"
        verbose_name_plural = "Варианты"


class UserResultOlympiad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    correct_answer = models.IntegerField(default=0, verbose_name='Количество правильных ответов')
    option = models.ForeignKey(VariantOlympiad, on_delete=models.CASCADE, verbose_name='Вариант олимпиады')
    file_answer = models.FileField(upload_to=content_file_name, validators=[validate_file_extension], blank=True, null=True, verbose_name='Файл с ответом на вопрос')
    time_start_olympiad = models.DateTimeField(auto_now_add=True, null=True, blank=True,
                                               verbose_name='Время начала олимпиады')
    end_start_olympiad = models.DateTimeField(auto_now_add=True, null=True, blank=True,
                                              verbose_name='Время окончания олимпиады')

    def __str__(self):
        return str(self.correct_answer)

    class Meta:
        verbose_name = "Результат олимпиады"
        verbose_name_plural = "Результаты олимпиад"
