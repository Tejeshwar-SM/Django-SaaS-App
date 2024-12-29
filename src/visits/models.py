from django.db import models
#models are the fields for the database
class PageVisit(models.Model):
    path = models.TextField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

