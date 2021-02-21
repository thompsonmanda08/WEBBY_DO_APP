from django.db import models


class Task(models.Model):
    task = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.task