from django.db import models
# Create your models here.


class User(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=25)
    # big_goals = models.ArrayField(models.ForeignKey(
    #     'Big_Goal', on_delete=models.CASCADE), null=True, blank=True)
    # days = models.ArrayField(models.ForeignKey(
    #     'Day', on_delete=models.CASCADE), null=True, blank=True)


class Big_Goal(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    timeframe = models.CharField(max_length=25)
    user_id = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='big_goals')


class Day(models.Model):
    date = models.DateField()
    user_id = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='days')


class List_Item(models.Model):
    day_id = models.ForeignKey(
        'Day', on_delete=models.CASCADE, null=True, related_name='list_items')
    body = models.CharField(max_length=150)
    category = models.CharField(max_length=50)
    big_goal_id = models.ForeignKey(
        'Big_Goal', on_delete=models.CASCADE, null=True, related_name='list_items')


class Notes(models.Model):
    body = models.TextField()
    day_id = models.ForeignKey(
        'Day', on_delete=models.CASCADE, null=True, related_name='notes')
    big_goal_id = models.ForeignKey(
        'Big_Goal', on_delete=models.CASCADE, null=True, related_name='notes')
