from django.contrib import admin
from pros.models import adminUser, Stat


# Register your models here.
@admin.register(adminUser)
class adminUserAdmin(admin.ModelAdmin):
    list_display = ["aNo", "id", "pw", "name", "authority", "mDate"]


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ["sNo", "member", "action", "where", "point", "sDate"]
