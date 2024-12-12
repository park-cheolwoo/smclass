from django.contrib import admin
from foodBoard.models import fBoard
# Register your models here.

@admin.register(fBoard)
class fBoardAdmin(admin.ModelAdmin):
  list_display = ["bNo","bTitle","bSubtitle",'bDate']

