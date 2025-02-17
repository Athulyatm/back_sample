from django.urls import path
from .views import *
urlpatterns = [
    path('add_student/',add_student, name ='add_student'),
    path('view_students/',view_students, name ='view_students'),
    path('view_student/<int:pk>',view_student, name ='view_student'),
    path('edit_student/<int:pk>',edit_student, name ='edit_student'),
    path('delete_student/<int:pk>',delete_student, name ='delete_student'),
]