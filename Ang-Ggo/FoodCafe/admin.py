from django.contrib import admin
from FoodCafe.models import Food, Foodinfo, Cafe, Cafeinfo


# Register your models here.
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ["fNo", "fName", "fCategory", "fLocation","fDate"]
    
@admin.register(Foodinfo)
class FoodinfoAdmin(admin.ModelAdmin):
    list_display = ["ffNo", "ffDate"]

@admin.register(Cafe)
class FoodAdmin(admin.ModelAdmin):
    list_display = ["cNo", "cName", "cCategory", "cLocation","cDate"]

@admin.register(Cafeinfo)
class FoodinfoAdmin(admin.ModelAdmin):
    list_display = ["ccNo", "ccDate"]