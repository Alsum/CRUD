from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from crud_sys import settings
from time import time

import logging
logr = logging.getLogger(__name__)

def get_upload_file_name(instance, filename):
    return settings.UPLOAD_FILE_PATTERN % (str(time()).replace('.','_'), filename)



class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    pic = models.FileField(upload_to=get_upload_file_name)
    url = models.URLField()
    mobile = models.CharField(blank=True, null=True,max_length=12)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
    	return self.user.username


class ServicePlan(models.Model):
	name=models.CharField(max_length=30)
	user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.name    
    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


@receiver(post_save, sender=User)
def make_sure_user_profile_is_added_on_user_created(sender, **kwargs):
    if kwargs.get('created', False):
        up = UserProfile.objects.create(user=kwargs.get('instance'))
        logr.debug("UserProfile created: %s" % up)
