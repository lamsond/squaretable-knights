from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('apply/', views.apply, name='apply'),
        path('enter_id/', views.get_id, name='get_id'),
        path('<int:student_id>/check_status/', views.check_status,
            name='check_status'),
        path('<int:student_id>/review/', views.review, name='review'),
        ]

