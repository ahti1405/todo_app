from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_main = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title