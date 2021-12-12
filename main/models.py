import logging
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone


logger = logging.getLogger(__name__)

# Create your models here.
class Repo(models.Model):
    file = models.FileField(upload_to='documents/', validators=[FileExtensionValidator(['pdf'])])
    title = models.CharField(max_length=120)
    status = models.BooleanField(default=True)
    date_upload = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.title}"