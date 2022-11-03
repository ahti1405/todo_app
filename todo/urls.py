from django.urls import path


from .views import TodoListView, TodoDetailView, TodoCreateView, TodoUpdateView, TodoDeleteView, HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('todo-list/', TodoListView.as_view(), name='todo_list'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='todo_detail'),
    path('todo/new/', TodoCreateView.as_view(), name='todo_create'),
    path('todo/edit/<int:pk>/', TodoUpdateView.as_view(), name='todo_update'),
    path('todo/delete/<int:pk>/', TodoDeleteView.as_view(), name='todo_delete'),
]