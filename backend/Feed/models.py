from django.db import models

class Feed(models.Model) :
    #get feed by default primary id

    #The same way as tistory
    title = models.TextField(default="Title")
    #Writer of the feed
    nickname = models.CharField(max_length=255, default="default")

    email = models.EmailField()
    #upload
    uploaded_at = models.DateTimeField(auto_now_add=True)

    content = models.TextField(default='')
    class Meta:
        db_table = 'Feed'

class Like(models.Model) :
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    
    #the person who liked the feed
    email = models.EmailField(default='a@google.com')

    #for toggle
    is_like = models.BooleanField(default=False)

    class Meta:
        db_table = "Like"

class Comment(models.Model) :
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    email = models.EmailField(default='a@google.com')
    content = models.TextField(default='')

    class Meta:
        db_table = "Comment"