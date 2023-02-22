from django.db import models
from pytz import timezone
# Create your models here.
class Image(models.Model) :
    name = models.TextField(default="default")
    uuid_name = models.TextField(default="")
    User = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Image'

    @property
    def created_at_korean_time(self):
        korean_timezone = timezone(settings.TIME_ZONE)
        return self.created_at.astimezone(korean_timezone)