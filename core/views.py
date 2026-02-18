from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from core.forms import LoginForm, SignupForm


def index_view(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        'index.html',
        {'login_form': LoginForm(request=request), 'signup_form': SignupForm()},
    )


@require_POST
def login_view(request: HttpRequest) -> HttpResponse:
    form = LoginForm(request=request, data=request.POST)
    if form.is_valid():
        login(request, form.get_user())
        messages.success(request, 'Вы успешно вошли в аккаунт.')
    else:
        messages.error(request, 'Неверный логин или пароль.')
    return redirect('index')


@require_POST
def signup_view(request: HttpRequest) -> HttpResponse:
    form = SignupForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, 'Аккаунт создан, вы вошли в систему.')
    else:
        for errors in form.errors.values():
            for error in errors:
                messages.error(request, error)
    return redirect('index')


@require_POST
def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    messages.info(request, 'Вы вышли из аккаунта.')
    return redirect('index')
