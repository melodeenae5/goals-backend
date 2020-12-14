from rest_framework import serializers
from .models import BigGoal, Day, ListItem, Note


class BigGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BigGoal
        fields = ('id', 'name', 'description', 'timeframe', 'owner')


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('id', 'date', 'owner')


class ListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListItem
        fields = ('id', 'day_id', 'body', 'category', 'big_goal_id')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'body', 'day_id', 'big_goal_id')
