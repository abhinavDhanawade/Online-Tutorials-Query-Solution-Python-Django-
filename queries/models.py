from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils import timezone
from services.models import Category
# Create your models here.

class QueryQuestion(models.Model):
    title = models.CharField(max_length=50, primary_key=True)
    catego = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    example = models.TextField(default="")
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    approval = models.NullBooleanField()

    def __str__(self):
        return self.title


class QuerySolution(models.Model):
    solution = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(QueryQuestion, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.solution



