from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True) 
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    
    priority = models.CharField(
        max_length=10,
        choices = [('L', 'Low'), ('M', 'Medium'), ('H', 'High')],
        default = 'L'
    )
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # class Meta:
    #     ordering = ['-created_at']
    #     verbose_name = 'Task'
    #     verbose_name_plural = 'Tasks'