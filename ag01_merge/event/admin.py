from django.contrib import admin
from event.models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
  list_display = ['aId','aDate','count','aTicket','usedTicket','aPoint']

