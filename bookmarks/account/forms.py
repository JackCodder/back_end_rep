from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    '''Форма для входа в систему'''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    '''Форма для модели пользователя'''
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        '''Метод для сравнения второго пароля с первым'''
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Пароли не совпадают.")
        return cd['password2']
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Этот электронный адрес уже занят.')
        return data
    

class UserEditForm(forms.ModelForm):
    '''Форма позволит пользователям редактировать свое имя, фамилию
    и адрес электронной почты, которые являются атрибутами модели User'''
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id)\
            .filter(email=data)
        if qs.exists():
            raise forms.ValidationError('Этот электронный адрес уже занят.')
        return data


class ProfileEditForm(forms.ModelForm):
    '''Форма позволит пользователям редактировать данные профиля,
    сохраненные в модели Profile'''
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']