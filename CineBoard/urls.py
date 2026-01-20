from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.regieter_view, name='register'),
    path('login/', views.auth_login_view, name='login'),
    path('user_list/', views.user_list_view, name='user_list'),
    path('logout/', views.auth_logout_view, name='logout'),
]


from django.urls import path
from .views import MovieListView, MovieUpdateView, MovieDeleteView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('edit/<int:pk>/', MovieUpdateView.as_view(), name='movie_edit'),
    path('delete/<int:pk>/', MovieDeleteView.as_view(), name='movie_delete'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movies.urls')),
]