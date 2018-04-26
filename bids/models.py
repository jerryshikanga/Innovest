from django.db import models
from django.contrib.auth.models import User
from campaigns.models import Campaign
from django.utils import timezone

# Create your models here.
class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)

    class Meta :
        """docstring for Meta """
        permissions = (('can_place_bid', 'Custom Can place a bid on a company'), ('can_view_bids', 'Custom Can View Bids'))
