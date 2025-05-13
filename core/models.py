from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
	class StatusChoices(models.TextChoices):
		PENDING = 'P', 'Pending'
		IN_PROGRESS = 'I', 'In progress'
		COMPLETED = 'C', 'Completed'

	class PriorityChoices(models.IntegerChoices):
		LOW = 1, 'Low'
		MEDIUM = 2, 'Medium'
		HIGH = 3, 'High'

	title = models.CharField(
			max_length=200,
			verbose_name='Title'
	)
	description = models.TextField(
			blank=True,
			null=True,
			verbose_name='Description'
	)
	status = models.CharField(
			max_length=20,
			choices=StatusChoices.choices,
			default=StatusChoices.PENDING,
			verbose_name='Status'
	)
	priority = models.IntegerField(
			choices=PriorityChoices.choices,
			default=PriorityChoices.MEDIUM,
			verbose_name='Priority'
	)
	due_date = models.DateField(
			blank=True,
			null=True,
			verbose_name='Due Date'
	)
	created_at = models.DateTimeField(
			auto_now_add=True,
			verbose_name='Created at'
	)
	updated_at = models.DateTimeField(
			auto_now=True,
			verbose_name='Updated at'
	)
	owner = models.ForeignKey(
			User,
			on_delete=models.CASCADE,
			related_name='tasks',
			verbose_name='Owner'
	)

	class Meta:
		ordering = [
			'due_date',
			'-priority',
			'created_at'
		]
		verbose_name = 'Task'
		verbose_name_plural = 'Tasks'

	def __str__(
			self
	):
		return self.title
