from django.contrib import admin

# Register your models here.
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('user_input_text', 'detected_intent', 'detected_intent_confidence')

admin.site.register(Message, MessageAdmin)
