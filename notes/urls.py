from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.NoteList.as_view()),
    url('<int:pk>/', views.NoteDetail.as_view())
]
