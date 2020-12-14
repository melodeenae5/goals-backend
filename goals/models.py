from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BigGoal(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    timeframe = models.CharField(max_length=25)
    owner = models.ForeignKey(
        'auth.User', related_name='big_goals', on_delete=models.CASCADE)


class Day(models.Model):
    date = models.DateField()
    owner = models.ForeignKey(
        'auth.User', related_name='days', on_delete=models.CASCADE)


class ListItem(models.Model):
    day_id = models.ForeignKey(
        Day, on_delete=models.CASCADE, null=True, related_name='list_items')
    body = models.CharField(max_length=150)
    category = models.CharField(max_length=50)
    big_goal_id = models.ForeignKey(
        BigGoal, on_delete=models.CASCADE, null=True, related_name='list_items')


class Note(models.Model):
    body = models.TextField()
    day_id = models.ForeignKey(
        Day, on_delete=models.CASCADE, null=True, related_name='notes')
    big_goal_id = models.ForeignKey(
        BigGoal, on_delete=models.CASCADE, null=True, related_name='notes')
