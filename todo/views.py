from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .models import Todo




class HomePageView(TemplateView):
    template_name = 'index.html'

class TodoListView(ListView):
    model = Todo
    context_object_name = 'todos'
    ordering = ['created']

    def get_queryset(self):
        # original qs
        qs = super().get_queryset() 
        # filter by author==user
        return qs.filter(author=self.request.user)
    

    


class TodoDetailView(DetailView):
    model = Todo



class TodoCreateView(CreateView):
    model = Todo
    fields = ('title', 'description', 'is_main', 'is_completed')
    success_url = reverse_lazy('todo_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TodoUpdateView(UserPassesTestMixin, UpdateView):
    model = Todo
    fields = ('title', 'description', 'is_main', 'is_completed')
    success_url = reverse_lazy('todo_list')

    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.author:
            return True
        return False


class TodoDeleteView(UserPassesTestMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')

    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.author:
            return True
        return False
