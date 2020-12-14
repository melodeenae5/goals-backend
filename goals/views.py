from django.shortcuts import render
from rest_framework import viewsets
from .models import BigGoal, Day, ListItem, Note
from .serializers import BigGoalSerializer, DaySerializer, ListItemSerializer, NoteSerializer

# Create your views here.


class BigGoalViewSet(viewsets.ModelViewSet):
    queryset = BigGoal.objects.all()
    serializer_class = BigGoalSerializer


class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer


class ListItemViewSet(viewsets.ModelViewSet):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
