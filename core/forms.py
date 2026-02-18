from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class SignupForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', max_length=150)
    email = forms.EmailField(label='Email', required=False)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    bio = forms.CharField(
        label='О себе',
        required=False,
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Расскажите о себе'}),
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
        }


class PortalTaskForm(forms.Form):
    title = forms.CharField(
        label='Новая задача',
        max_length=120,
        widget=forms.TextInput(attrs={'placeholder': 'Например: Подготовить отчёт'}),
    )


class AnnouncementForm(forms.Form):
    text = forms.CharField(
        label='Объявление',
        max_length=180,
        widget=forms.TextInput(attrs={'placeholder': 'Добавьте короткое объявление для команды'}),
    )
