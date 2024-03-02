import uuid
from django.db import models

# Create your models here.
class Note(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=300, null=False, blank=False)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    