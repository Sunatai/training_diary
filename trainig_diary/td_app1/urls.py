from django.urls import path
from .views import DiaryList, DiaryDetail, DiaryCreate, DiaryDelete, DiaryUpdate

urlpatterns = [
    path('', DiaryList.as_view(), name='list'),
    path('detail/<int:pk>', DiaryDetail.as_view(), name='detail'),
    path('create/', DiaryCreate.as_view(), name='create'),
    path('delete/<int:pk>', DiaryDelete.as_view(), name='delete'),
    path('update/<int:pk>', DiaryUpdate.as_view(), name='update'),
]
