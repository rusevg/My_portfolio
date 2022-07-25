from django.db import models
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title

class CommentPost(models.Model):

    class Meta():
        db_table = 'comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.blog)

    blog_c = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField('Text of comment', )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    moderation = models.BooleanField(default=False)
