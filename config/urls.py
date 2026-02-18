from django.contrib import admin
from django.urls import path

from core.views import (
    index_view,
    login_view,
    logout_view,
    portal_home_view,
    profile_view,
    signup_view,
    task_delete_view,
    task_toggle_view,
    tasks_view,
    team_board_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('portal/', portal_home_view, name='portal_home'),
    path('portal/profile/', profile_view, name='profile'),
    path('portal/tasks/', tasks_view, name='tasks'),
    path('portal/tasks/<int:index>/toggle/', task_toggle_view, name='task_toggle'),
    path('portal/tasks/<int:index>/delete/', task_delete_view, name='task_delete'),
    path('portal/team-board/', team_board_view, name='team_board'),
]
