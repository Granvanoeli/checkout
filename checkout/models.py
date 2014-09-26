from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_pictures', blank=True, default='profile_pictures/default.png')
    location = models.CharField(max_length=100)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)

    def image_tag(self):
        return u'<img src="%s" height = 100 />' % (self.picture.url)
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __unicode__(self):
        return self.user.username


class List(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    total_check = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

class Item (models.Model):
    list = models.ForeignKey(List)
    item_text = models.CharField(max_length=200)
    done = models.BooleanField(default=False)

    def __unicode__(self):
        return self.item_text
