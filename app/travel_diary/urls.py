from django.urls import path

from .views import DiaryCreateView, DiaryListView, DiaryDetailView

app_name = 'diaries'
urlpatterns = [
    path('', DiaryListView.as_view(), name='index'),
    path('create', DiaryCreateView.as_view(), name='create'),
    path('<slug:slug>', DiaryDetailView.as_view(), name='detail'),
]