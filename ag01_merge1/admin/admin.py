from django.contrib import admin
from admin.models import adminUser,Stat
# Register your models here.
@admin.register(adminUser)
class adminUserAdmin(admin.ModelAdmin):
    list_display = ["aNo", "id", "pw", "name", "authority", "mdate"]


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ["sNo", "member", "action", "where", "point", "sDate"]
