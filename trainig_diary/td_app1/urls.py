from django.urls import path
from .views import DiaryList, DiaryDetail, DiaryCreate, DiaryDelete, DiaryUpdate, DiaryTest, signupfunc,loginfunc, listfunc, logoutfunc

urlpatterns = [
    #path('', DiaryList.as_view(), name='list'),
    path('', listfunc, name='list'),
    path('detail/<int:pk>', DiaryDetail.as_view(), name='detail'),
    path('create/', DiaryCreate.as_view(), name='create'),
    path('delete/<int:pk>', DiaryDelete.as_view(), name='delete'),
    path('update/<int:pk>', DiaryUpdate.as_view(), name='update'),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
]
