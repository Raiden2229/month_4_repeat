from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from users.forms import CustomRegisterForm
from users.models import CustomUser
from users.forms import CustomLoginForm


#REGISTER
def regieter_view(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = CustomRegisterForm()

    return render(
            request,
            template_name='users/register.html',
            context={'form': form}
        )


#АВТОРИЗАЦИЯ
def auth_login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/user_list/')
    else:
        form = CustomLoginForm()

    return render(
        request,
        template_name='users/login.html',
        context={'form': form}
    )


def auth_logout_view(request):
    logout(request)
    return redirect('/login/')


def user_list_view(request):
    if request.method == 'GET':
        user_list = CustomUser.objects.all()
        return render(
            request,
            template_name='users/user_list.html',
            context={'user_list': user_list}
        )
    



from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Movie

class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Movie.objects.filter(title__icontains=query)
        return Movie.objects.all()


class MovieUpdateView(UpdateView):
    model = Movie
    fields = ['title', 'description', 'genre', 'release_date', 'rating', 'tag']
    template_name = 'movies/movie_form.html'
    success_url = reverse_lazy('movie_list')


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')
