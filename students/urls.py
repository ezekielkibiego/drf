from django.urls import path
from students.views import *

urlpatterns = [
    path('api/students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('api/students/<int:id>/', StudentDetailView.as_view(), name='students-detail'),
]