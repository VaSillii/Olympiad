from django import forms
from django.contrib.auth.models import User


class FormEditProfile(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(), label="Email:")
    username = forms.CharField(max_length=150, label="Имя пользователя:")
    surname = forms.CharField(max_length=100, label="Фамилия:")
    name = forms.CharField(max_length=100, label="Имя:")

    def __init__(self, *args, **kwargs):
        super(FormEditProfile, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['surname'].widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.first_name = self.cleaned_data['name']
            user.last_name = self.cleaned_data['surname']
            user.email = self.cleaned_data['email']
            user.username = self.cleaned_data['username']
            user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'email',)