from django.contrib import admin
from home.models import SearchMapInfo

@admin.register(SearchMapInfo)
class SearchMapInfoAdmin(admin.ModelAdmin):
  list_display=['sInput','sLocation','sMenu','sKeyword','sName']

