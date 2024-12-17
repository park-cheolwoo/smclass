from django.contrib import admin
from foodBoard.models import fBoard,fTime
# Register your models here.

@admin.register(fBoard)
class fBoardAdmin(admin.ModelAdmin):
    list_display = ["bNo","bTitle","bSubtitle",'bDate']


@admin.register(fTime)
class fTimeAdmin(admin.ModelAdmin):
    list_display = ["fNo", "member", "fboard", "fPeople", "fTime", "fDate"]
