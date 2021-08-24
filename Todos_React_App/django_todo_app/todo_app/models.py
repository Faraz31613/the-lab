from django.db import models

# Create your models here.
class Todo(models.Model):
    todo_text = models.CharField(max_length=300)

    def __str__(self):
        return self.todo_text
