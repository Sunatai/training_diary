from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TrainingDiaryModel
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
class DiaryList(ListView):
    template_name = 'list.html'
    model = TrainingDiaryModel #どのモデルを使用するかの指定

class DiaryDetail(DetailView):
    template_name = 'detail.html'
    model = TrainingDiaryModel #どのモデルを使用するかの指定

class DiaryCreate(CreateView):
    template_name = 'create.html'
    model = TrainingDiaryModel
    fields = ('body_part','train_name','weight','raise_times','set_times','date','memo', 'author')
    success_url = reverse_lazy('list')

class DiaryDelete(DeleteView):
    template_name = 'delete.html'
    model = TrainingDiaryModel
    success_url = reverse_lazy('list')

class DiaryUpdate(UpdateView):
    template_name = 'update.html'
    model = TrainingDiaryModel
    fields = ('body_part','train_name','weight','raise_times','set_times','date','memo')
    success_url = reverse_lazy('list')

class DiaryTest(ListView):
    template_name = 'test.html'
    model = TrainingDiaryModel



def signupfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html',{'error': 'このユーザーは既に登録されています'})
        except:
            user = User.objects.create_user(username2, '', password2)
            return redirect('login')
        #return render(request, 'signup.html', {'some': 100})
    else:
        print('not POST')
    return render(request, 'signup.html', {'some': 100})


def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')


@login_required
def listfunc(request):
    now_user = request.user.get_username() #ログインしているユーザーを取得できる
    #object_list = TrainingDiaryModel.objects.get(author=now_user)
    object_list = TrainingDiaryModel.objects.all()
    return render(request, 'list_new.html', {'object_list': object_list})


def logoutfunc(request):
    logout(request)
    return redirect('login')
