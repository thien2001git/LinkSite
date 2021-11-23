from django.db import models


# Create your models here.
class Type(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class Links(models.Model):
    idType = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.TextField()
