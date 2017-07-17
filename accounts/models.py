from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.urls import reverse

from django.core.cache import cache
import datetime

def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class Profile(models.Model):
    user = models.OneToOneField(User)
    interests = models.TextField(max_length=100, default="")
    image = models.ImageField(
        upload_to=upload_location,
        null=True, blank=True,
        height_field='height_field',
        width_field='width_field',
    )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,
                                       related_name="followers")

    def get_absolute_url(self):
        return reverse("accounts:detail", kwargs={"slug": self.user})

    def get_edit_url(self):
        return reverse("accounts:edit", kwargs={"slug": self.user})

    def get_follow_instances(self):
        return self.followers.all()

    # def last_seen(self):
    #     return cache.get('seen_%s' % self.user.username)
    #
    # def online(self):
    #     if self.last_seen():
    #         now = datetime.datetime.now()
    #         if now > self.last_seen() + datetime.timedelta(
    #                      seconds=settings.USER_ONLINE_TIMEOUT):
    #             return False
    #         else:
    #             return True
    #     else:
    #         return False


    # def get_follow_url(self):
    #     return reverse("accounts:follow_toggle", kwargs={"slug": self.slug})

    @property
    def get_instance_centent_type(self):
        return ContentType.objects.get_for_model(self.__class__)


def create_profile(sender, instance, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=instance)
        user_profile.save()


post_save.connect(create_profile, sender=User)
