from django.shortcuts import render
from rest_framework import viewsets
from .models import Big_Goal, Day, List_Item, Note
from .serializers import Big_GoalSerializer, DaySerializer, List_ItemSerializer, NoteSerializer

# Create your views here.


class Big_GoalViewSet(viewsets.ModelViewSet):
    queryset = Big_Goal.objects.all()
    serializer_class = Big_GoalSerializer


class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer


class List_ItemViewSet(viewsets.ModelViewSet):
    queryset = List_Item.objects.all()
    serializer_class = List_ItemSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
