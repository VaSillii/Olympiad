from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from .models import VariantOlympiad, UserResultOlympiad


@login_required(login_url='login')
def get_olympiad(request):
    option = VariantOlympiad.objects.all()
    context = {
        'option': option
    }
    return render(request, 'olympiad_template.html', context=context)


@login_required(login_url='login')
def get_option(request, index_option):
    option = get_object_or_404(VariantOlympiad, pk=index_option)
    paginator = Paginator(option.questions.all(), 1)
    page = request.GET.get('page')
    questions = paginator.get_page(page)

    date = request.POST.get('time_start', False)
    date = timezone.now if date else timezone.now

    data = {}
    if request.method == 'POST':
        correct_answer = 0

        for qsn in option.questions.all():
            answer = request.POST.get(str(qsn.id), False).lower()
            data[qsn.id] = answer
            if answer == qsn.answer.lower():
                correct_answer += 1

        if request.GET.get('submit', False) == 'yes':
            UserResultOlympiad.objects.create(
                user=request.user,
                correct_answer=correct_answer,
                option=option,
                time_start_olympiad=date,
                end_start_olympiad=timezone.now,
            )
            return redirect('accounts:my_olympiad')

    context = {
        'option': option,
        'questions': questions,
        'time_start': date,
        'question_val': data,
    }

    # if request.method == 'POST':
    #     correct_answer = 0
    #
    #     for qsn in option.questions.all():
    #         answer = request.POST.get(str(qsn.id), False).lower()
    #         if answer == qsn.answer.lower():
    #             correct_answer += 1
    #     date = request.POST.get('time_start', False)
    #     UserResultOlympiad.objects.create(
    #         user=request.user,
    #         correct_answer=correct_answer,
    #         option=option,
    #         time_start_olympiad=date,
    #         end_start_olympiad=timezone.now,
    #     )
    #     return redirect('accounts:my_olympiad')

    return render(request, 'question_olympiad.html', context=context)
