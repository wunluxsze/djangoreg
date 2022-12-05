from django import forms

# Create your views here.
class UserForm(forms.Form):
    name = forms.CharField(widget= forms.TextInput(attrs={"class": "name flex input", "placeholder": "Логин"}), required= True, label='Введите имя')
    email = forms.EmailField(widget= forms.EmailInput(attrs={"class": "email flex input", "placeholder": "Почта"}), required= True, label='Введите Email')
    password = forms.CharField(widget= forms.PasswordInput(attrs={"class": "password flex input", "placeholder": "Пароль"}), required= True, label='Введите пароль')

class UserSign(forms.Form):
    name = forms.CharField(widget= forms.TextInput(attrs={"class": "name flex input", "placeholder ": "Логин"}), required= True, label='Введите имя')
    password = forms.CharField(widget= forms.PasswordInput(attrs={"class": "password flex input", "placeholder": "Пароль"}), required= True, label='Введите пароль')