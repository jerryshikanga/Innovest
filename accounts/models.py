from django.db import models

# Create your models here.
class UserProfile(models.Model):
    """docstring for UserProfile."""
    def __init__(self, arg):
        super(UserProfile, self).__init__()
        self.arg = arg
