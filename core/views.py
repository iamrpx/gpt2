from __future__ import annotations

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from core.forms import (
    AnnouncementForm,
    LoginForm,
    PortalTaskForm,
    ProfileForm,
    SignupForm,
)


PORTAL_NEWS = [
    'Обновлён регламент по отпускам — проверьте раздел HR.',
    'В пятницу в 16:00 общий созвон по квартальным целям.',
    'Открыт набор идей на улучшение внутренних процессов.',
]


def index_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect('portal_home')
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
        return redirect('portal_home')

    messages.error(request, 'Неверный логин или пароль.')
    return redirect('index')


@require_POST
def signup_view(request: HttpRequest) -> HttpResponse:
    form = SignupForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, 'Аккаунт создан, вы вошли в систему.')
        return redirect('portal_home')

    for errors in form.errors.values():
        for error in errors:
            messages.error(request, error)
    return redirect('index')


@require_POST
@login_required
def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    messages.info(request, 'Вы вышли из аккаунта.')
    return redirect('index')


@login_required
def portal_home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'portal/home.html', {'news': PORTAL_NEWS})


@login_required
def profile_view(request: HttpRequest) -> HttpResponse:
    bio = request.session.get('profile_bio', '')
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            request.session['profile_bio'] = form.cleaned_data['bio']
            messages.success(request, 'Профиль обновлён.')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user, initial={'bio': bio})

    return render(request, 'portal/profile.html', {'form': form, 'bio': bio})


@login_required
def tasks_view(request: HttpRequest) -> HttpResponse:
    tasks = request.session.get('portal_tasks', [])

    if request.method == 'POST':
        form = PortalTaskForm(request.POST)
        if form.is_valid():
            tasks.append({'title': form.cleaned_data['title'], 'done': False})
            request.session['portal_tasks'] = tasks
            messages.success(request, 'Задача добавлена.')
            return redirect('tasks')
    else:
        form = PortalTaskForm()

    return render(request, 'portal/tasks.html', {'form': form, 'tasks': tasks})


@require_POST
@login_required
def task_toggle_view(request: HttpRequest, index: int) -> HttpResponse:
    tasks = request.session.get('portal_tasks', [])
    if 0 <= index < len(tasks):
        tasks[index]['done'] = not tasks[index]['done']
        request.session['portal_tasks'] = tasks
        messages.info(request, 'Статус задачи изменён.')
    return redirect('tasks')


@require_POST
@login_required
def task_delete_view(request: HttpRequest, index: int) -> HttpResponse:
    tasks = request.session.get('portal_tasks', [])
    if 0 <= index < len(tasks):
        del tasks[index]
        request.session['portal_tasks'] = tasks
        messages.info(request, 'Задача удалена.')
    return redirect('tasks')


@login_required
def team_board_view(request: HttpRequest) -> HttpResponse:
    announcements = request.session.get('announcements', [])

    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcements.insert(0, form.cleaned_data['text'])
            request.session['announcements'] = announcements[:10]
            messages.success(request, 'Объявление опубликовано.')
            return redirect('team_board')
    else:
        form = AnnouncementForm()

    return render(
        request,
        'portal/team_board.html',
        {'form': form, 'announcements': announcements},
    )
