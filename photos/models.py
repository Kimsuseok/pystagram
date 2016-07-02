from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse_lazy

# Create your models here.
class Photo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=300)
    content = models.TextField()
    image = models.ImageField(upload_to='%Y/%m/%d', null=True, blank=True)
    description = models.TextField(max_length=500,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse_lazy('photos:view_photo', kwargs= {'pk':self.pk})
        # return '/photos/{}/'.format(self.pk)

class Comment(models.Model):
    photo = models.ForeignKey(Photo, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}: {}'.format(self.pk, self.content)