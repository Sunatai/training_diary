from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TrainingDiaryModel
from django.urls import reverse_lazy

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
    fields = ('body_part','train_name','weight','raise_times','set_times','date','memo')
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
