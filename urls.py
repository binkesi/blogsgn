from django.urls import path
from . import views

app_name = 'blogsgn'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ArticleView.as_view(), name='detail')
]