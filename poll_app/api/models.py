from django.db import models
import string
import random

def unique_code():
    length = 8
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break
    return code

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=48, unique=True)
    poll_q = models.CharField(max_length=80, default="")
    created = models.DateTimeField(auto_now_add=True)


class Poll(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    poll_a = models.CharField(max_length=50, default="")
    votes_up = models.IntegerField(null=False, default=0)
    votes_down = models.IntegerField(null=False, default=0)
    created = models.DateTimeField(auto_now_add=True)

