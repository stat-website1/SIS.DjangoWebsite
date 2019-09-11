from django.db import models

# Create your models here.

class Message(models.Model):
    user_input_text = models.CharField(max_length=100)
    detected_intent = models.CharField(max_length=255)
    detected_intent_confidence = models.CharField(max_length=255)
    chatbot_output_text = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
