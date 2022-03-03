from django.urls import path
from . import views

urlpatterns = [
    path('', views.table),
    path('tables/<int:id>/', views.booktable),
    path('tables/clear/<int:id>/',views.cleartable)
]