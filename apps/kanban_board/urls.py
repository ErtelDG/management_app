from django.urls import path

from . import views

urlpatterns = [
    path('', views.kanban_board, name='kanban_board'),
]