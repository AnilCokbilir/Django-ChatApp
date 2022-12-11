from django.contrib import admin
from .models import Message, Chat
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    fields = ('chat','text','created_at', 'author', 'receiver')
    list_display = ('created_at', 'author', 'text', 'receiver')
    

admin.site.register(Message,MessageAdmin)
admin.site.register(Chat)