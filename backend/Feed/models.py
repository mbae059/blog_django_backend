from django.db import models

class Feed(models.Model) :
    #get feed by default primary id

    #The same way as tistory
    title = models.TextField(default="Title")
    #Writer of the feed
    nickname = models.CharField(max_length=255)

    email = models.EmailField()
    #upload
    uploaded_at = models.DateTimeField(auto_now_add=True)

    content = models.TextField(default='')
    class Meta:
        db_table = 'Feed'

class Like(models.Model) :
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(default='a@google.com')
    is_like = models.BooleanField(default=False)

    class Meta:
        db_table = "Like"

class Comment(models.Model) :
    feed_id = models.IntegerField(default = 0)
    email = models.EmailField(default='a@google.com')
    content = models.TextField(default='')

    class Meta:
        db_table = "Comment"