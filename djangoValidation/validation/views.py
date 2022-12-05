
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from .forms import UserSign


def index(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data['name']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']
            return HttpResponse(f' {name}, поздравляю с регистрацией! <br> Указанные вами данные: <br> Имя - {name}, <br> Пароль - {password}, <br> Емаил -{email}')
        return render(request, "index.html", {"form": userform})
    userform = UserForm()
    return render(request, "index.html", {"form": userform})

def sign(request):
    if request.method == "POST":
        usersign = UserSign(request.POST)
        if usersign.is_valid():
            name = usersign.cleaned_data['name']
            password = usersign.cleaned_data['password']
            if name == 'User1' and password == '12345678':
                return HttpResponse(f'Поздравляю с успешным входом')
            else:
                return redirect('register')
        return render(request, "sign.html", {"form": usersign})
    usersign = UserSign()
    return render(request, "sign.html", {"form": usersign})