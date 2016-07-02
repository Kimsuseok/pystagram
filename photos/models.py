from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse_lazy

# Create your models here.
class Photo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    image = models.ImageField(upload_to='%Y/%m/%d')
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse_lazy('photos:detail', kwargs= {'pk':self.pk})
        # return '/photos/{}/'.format(self.pk)