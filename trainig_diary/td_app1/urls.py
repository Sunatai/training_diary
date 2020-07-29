from django.urls import path
from .views import DiaryList, DiaryDetail, DiaryCreate, DiaryDelete, DiaryUpdate, DiaryTest, hello_template
from . import views

urlpatterns = [
    path('', DiaryList.as_view(), name='list'),
    path('template/', views.hello_template, name='graph'),
    path('detail/<int:pk>', DiaryDetail.as_view(), name='detail'),
    path('create/', DiaryCreate.as_view(), name='create'),
    path('delete/<int:pk>', DiaryDelete.as_view(), name='delete'),
    path('update/<int:pk>', DiaryUpdate.as_view(), name='update'),
    path('test/', DiaryTest.as_view(), name='test'),
]
