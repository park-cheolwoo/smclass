from django.contrib import admin
from students.models import Student

# admin 사이트에 컬럼 보여지는 부분 추가
class StudentAdmin(admin.ModelAdmin):
  list_display = ['s_name','s_major','s_age']

# admin 사이트에 추가
admin.site.register(Student,StudentAdmin)
