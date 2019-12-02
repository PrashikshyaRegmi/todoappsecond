from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name="home"),
    path(r'<list_id>/^delete/',views.delete,name="delete"),
    path(r'<list_id>/^completed/',views.completed,name="completed"),
    path(r'<list_id>/^uncompleted/',views.uncompleted,name="uncompleted"),
    path('edit/<int:pk>/',views.edit,name="edit"),
]
