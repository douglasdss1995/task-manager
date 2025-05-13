from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
	owner_username = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Task
		fields = [
			'id',
			'title',
			'description',
			'status',
			'priority',
			'due_date',
			'created_at',
			'updated_at',
			'owner',
			'owner_username'
		]
		read_only_fields = [
			'created_at',
			'updated_at'
		]
