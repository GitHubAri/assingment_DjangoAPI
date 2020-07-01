from django.contrib import admin

from .models import Students


class StudentsList(admin.ModelAdmin):
    list_display = ('roll_no','name', 'age', 'marks')
    list_filter = ('roll_no', 'name')
    search_fields = ('roll_no', 'name')

admin.site.register(Students, StudentsList)
