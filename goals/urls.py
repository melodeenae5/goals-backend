# from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import BigGoalViewSet, DayViewSet, ListItemViewSet, NoteViewSet

router = DefaultRouter()
router.register(r'big_goals', BigGoalViewSet, basename='big_goal')
router.register(r'days', DayViewSet, basename='day')
router.register(r'list_items', ListItemViewSet, basename='list_item')
router.register(r'notes', NoteViewSet, basename='note')
urlpatterns = router.urls

# urlpatterns = [
#     path('', include('djoser.urls')),
#     path('', include('djoser.urls.authtoken'))
# ]
