from rest_framework import viewsets

from todo.models import Todo
from todo.serializer import TodoSerializer


class TodoModelViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer