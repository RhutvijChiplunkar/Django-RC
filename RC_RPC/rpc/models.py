from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class details(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    ph_no=models.IntegerField()
    year=models.CharField(max_length=10)
    score=models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
