from django.db import models
from django.db.models import Sum, Count, F
from django.contrib.auth.models import User
from django.utils import timezone

class CampaignManager(models.Manager):
    """docstring for CampaignManager."""
    def get_queryset(self):
        return super().get_queryset().annotate(Count('bid'), sum_bids = Sum('bid__amount'), percentage_raised = (Sum('bid__amount')/F('funding_requirement'))).order_by('-date_added')

class Category(models.Model):
    """docstring for Category."""
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=60000)
    picture = models.ImageField(upload_to='uploads/category')

    class Meta :
        """docstring for Meta ef __init__(self, arg):"""
        verbose_name_plural = 'Categories'
        ordering = ['name']
        permissions = (('can_add_category', 'Custom Can add a Category'), ('can_update_category', 'Custom Can edit a Category'), ('can_delete_category', 'Custom Can delete a Category'))

    def __str__(self):
        return self.name

# Create your models here.
class Campaign(models.Model):
    """docstring for  Campaign."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    summary_text = models.CharField(max_length=1000)
    description = models.TextField(max_length=60000)
    funding_requirement = models.DecimalField(max_digits=20, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    picture = models.ImageField(upload_to='uploads/campaign/')
    date_start = models.DateTimeField(default=timezone.now)
    date_end = models.DateTimeField()

    objects = CampaignManager()

    class Meta :
        """docstring for Meta."""
        verbose_name_plural = 'Campaigns'
        ordering = ['name']
        permissions = (('can_add_campaign', 'Custom Can add a campaign'), ('can_update_campaigm', 'Custom Can edit a campaign'), ('can_delete_campaign', 'Custom Can delete a campaign'), )

    def __str__(self):
        return self.name

    def add_funds(self, amount):
        self.current_funding += amount
        self.save()

    def is_fully_funded(self):
        amount_raised = Campaign.objects.get(id=self.id).sum_bids
        if amount_raised >= self.funding_requirement :
            return True
        else :
            return False

    def get_percentage_raised(self):
        amount_raised = Campaign.objects.get(id=self.id).sum_bids
        return amount_raised/self.funding_requirement * 100
