from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('courses/destroy/<int:current_id>', views.remove),
    path('courses/destroy/<int:current_id>/delete', views.delete)
]