from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Stream(models.Model):
    # Stream keys are effectively available to any user, but RTMP has no concept
    # of users so we cannot have per-user keys
    key = models.CharField(max_length=64, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.TextField(blank=True)
    live_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{}.{}".format(self.id, self.user)

    def is_live(self):
        return self.live_at is not None
