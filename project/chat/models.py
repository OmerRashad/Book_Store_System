from django.db import models

class Word (models.Model):
    id              = models.AutoField(primary_key=True)
    roomName        = models.CharField(max_length = 15, null = True)
    count           = models.IntegerField(default = 0,null = True)
    def __str__(self):
        return self.roomName