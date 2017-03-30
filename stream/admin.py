from django.contrib import admin

# Register your models here.
from .models import Stream

class StreamAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_live',)
admin.site.register(Stream, StreamAdmin)
