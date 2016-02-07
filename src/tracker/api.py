from tastypie.resources import ModelResource

from .models import UserProfile

class ProfileResource(ModelResource):

    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = 'profile'