from django.db import models

class Feed(models.Model) :
    #get feed by default primary id
    #The same way as tistory
    title = models.TextField(default="default")
    email = models.EmailField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Feed'
