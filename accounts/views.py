from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from variant.models import UserResultOlympiad
from .forms import FormEditProfile


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = FormEditProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    form = FormEditProfile()
    context = {
        'form': form,
    }
    return render(request, 'profile.html', context=context)


@login_required
def my_olympiad_view(request):
    olympiads = UserResultOlympiad.objects.filter(user=request.user)
    context = {
        'olympiads': olympiads,
    }
    return render(request, 'my-olympiad.html', context=context)

