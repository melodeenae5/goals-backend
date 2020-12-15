from django.contrib import admin
from .models import BigGoal, Day, ListItem, Note

# Register your models here.

admin.site.register(BigGoal)
admin.site.register(Day)
admin.site.register(ListItem)
admin.site.register(Note)
