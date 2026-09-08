from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:note_id>/confirmar', views.delete, name='delete'),
    path('notes/<int:note_id>/edit/', views.edit, name='edit'),
]