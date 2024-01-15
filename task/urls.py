from django.urls import path

from . import views


urlpatterns = [
  path('', views.index, name='home')
]


htmxpatterns = [
  path('create_task/', views.create_task, name='create_task'),
  path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
  path('mark_task/<int:pk>/', views.mark_task, name='mark_task'),
]

urlpatterns += htmxpatterns
