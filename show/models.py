from django.db import models

#from django.contrib.auth.models import (    AbstractBaseUser, PermissionsMixin, BaseUserManager)
# Create your models here.

class enter(models.Model):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
 
    """
    name = models.CharField(max_length=40)
    contact_number = models.IntegerField(max_length=30)
    object = models.Manager()
    def __unicode__(self):
        return '%s %s' % (self.name, self.contact_number)