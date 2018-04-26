from django.shortcuts import render
from campaigns.models import Campaign, Category

def index(request, *args, **kwargs) :
    context = {
        'campaigns': Campaign.objects.all().order_by('-date_start'),
        'categories': Category.objects.all(),
    }
    return render(request, 'index.html', context)
