from django.contrib import admin
from .models import Message, Chat

class MessageAdmin(admin.ModelAdmin):
    fields = ('chat','text', 'created_at','author','receiver')
    list_display = ('author','receiver','text', 'created_at')
    search_fields = ('text',)

admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)
