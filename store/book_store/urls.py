from django.urls import path
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/list/<str:status>', views.book_list, name='book_list'),
    path('book/<int:pk>', views.book_detail, name='book_detail'),
    path('book/new/', views.book_new, name='book_new'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('book/<int:pk>/book_change_status/', views.book_change_status, name='book_change_status'),
    path('book/<int:pk>/remove/', views.book_remove, name='book_remove'),
    path('book/requests/', views.view_requests, name='requests'),
    path('accounts/login/', login, name='login'),
    path('accounts/logout/', logout,{'next_page': '/book_store'}, name='logout',),
]
