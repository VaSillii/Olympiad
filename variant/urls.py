from django.urls import path

from variant.views import get_olympiad, get_option

app_name = 'variant'

urlpatterns = [
    path('select-olympiade/', get_olympiad, name='olympiad'),
    path('question-olympiad/<int:index_option>/', get_option, name='question_olympiad'),
]