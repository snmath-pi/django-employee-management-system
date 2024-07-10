from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('all-emp/', views.all_emp, name='all_emp'),
    path('add-emp/', views.add_emp, name='add_emp'),
    path('remove-emp/<int:e_id>', views.remove_emp, name='remove_emp'),
    path('remove-emp/', views.remove_emp, name='remove_emp'),
    path('filter-emp/', views.filter_emp, name='filter_emp'),
]
