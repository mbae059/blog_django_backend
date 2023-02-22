from django.db import models
# Create your models here.
class Feed(models.Model) :
    name = models.TextField(default="default")
    uuid_name = models.UUIDField(unique=True) #get Feed by uuid_name
    userEmail = models.EmailField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Image'
