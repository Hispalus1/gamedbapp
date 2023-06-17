from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('seznam/', views.games, name='game_list'),
 path('seznamD/', views.developer, name='developer_list'),
 path('seznam/<int:pk>', views.GameDetailView.as_view(), name='game_detail'),
 path('seznamD/<int:pk>', views.DeveloperDetailView.as_view(), name='developer_detail'),
]