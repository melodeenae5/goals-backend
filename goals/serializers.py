from rest_framework import serializers
from .models import Big_Goal, Day, List_Item, Note


class Big_GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Big_Goal
        fields = ('id', 'name', 'description', 'timeframe', 'owner')


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('id', 'date', 'owner')


class List_ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model: List_Item
        fields = ('id', 'day_id', 'body', 'category', 'big_goal_id')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model: Note
        fields = ('id', 'body', 'day_id', 'big_goal_id')
