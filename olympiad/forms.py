from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserFormRegister(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(), label="Email:")
    username = forms.CharField(max_length=150, label="Имя пользователя:")
    surname = forms.CharField(max_length=100, label="Фамилия:")
    name = forms.CharField(max_length=100, label="Имя:")
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.first_name = self.cleaned_data['name']
            user.last_name = self.cleaned_data['surname']
            user.email = self.cleaned_data['email']
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UserFormRegister, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['surname'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
