# coding: utf-8
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.views.generic.base import View


class LoginView(View):
    def get(self, request):
        step_next = request.GET.get('next', '/')
        return render(request, 'web/login.html', {'next': step_next})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        step_next = request.POST.get('next', '/')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # success
            auth_login(request, user)
            return redirect(step_next)
        else:
            # failed
            context = {"msg": "用户名或密码错误", "next": step_next}
            return render(request, 'web/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('/accounts/login/')


@login_required
def demo(request):
    return render(request, 'web/demo.html', {'nbar': 'users'})