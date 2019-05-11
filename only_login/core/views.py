from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from core import models



class IndexPage(View):
    def get(self, request):

        return render(request, 'i.html', {

        })


class SignUp(View):

    def get(self, request):
        return render(request, 'sign_up.html')

    def post(self, request):

        login = request.POST['login']
        password = request.POST['password']

        if not models.User.objects.filter(login=login, password=password):
            new_user = models.User(login=login, password=password)
            new_user.save()

        else:
            login_exist = login

            return render(request, 'i.html', {
                'login_exist': login_exist
            })

        request.session['user_id'] = new_user.id




        return redirect('/')


class Exit(View):
    def get(self, request):

        if request.session.get('user_id'):

            request.session.pop('user_id')

        return redirect('/')


class Login(View):
    def get(self, request):

        return render(request, 'login.html')

    def post(self, request):

        input_login = request.POST['login']
        input_password = request.POST['password']

        try:
            new_user = models.User.objects.get(login=input_login, password=input_password)

        except models.User.DoesNotExist as e:
            return HttpResponse(f'user {input_login} doesnt exist')

        request.session['user_id'] = new_user.id

        return redirect('/')


