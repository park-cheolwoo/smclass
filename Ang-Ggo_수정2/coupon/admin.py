from django.contrib import admin
from coupon.models import Coupon

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
  list_display = ['member','discount','used_from','used_to']
