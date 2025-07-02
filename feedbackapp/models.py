from django.db import models
from django.utils.timezone import now
from accountapp.models import CustomUser

class Feedback(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField(null=False, blank=False)
    emoji = models.CharField(max_length=10, blank=True, null=True)
    comment = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(default=now)
    contains_bad_words = models.BooleanField(default=False)
    bad_words_used = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.rating} stars'
