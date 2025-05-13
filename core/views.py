from rest_framework import viewsets, permissions

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
	"""
	API endpoint que permite tarefas serem visualizadas, editadas ou deletadas.
	"""
	queryset = Task.objects.all()
	serializer_class = TaskSerializer
	permission_classes = [
		permissions.IsAuthenticated
	]

	def perform_create(
			self,
			serializer
	):
		# Define o usuário atual como o proprietário da tarefa
		serializer.save(owner=self.request.user)

	def get_queryset(
			self
	):
		# Filtra tarefas para mostrar apenas as do usuário atual
		return Task.objects.filter(owner=self.request.user)
