from django.urls import path

from . import views

app_name = 'poop'

urlpatterns = [
    path('', views.home, name='home'),
    path('Q&A/', views.QnA, name='QnA'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]