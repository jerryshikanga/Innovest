# Generated by Django 2.0.3 on 2018-04-23 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('summary_text', models.CharField(max_length=1000)),
                ('description', models.TextField(max_length=60000)),
                ('funding_requirement', models.DecimalField(decimal_places=2, max_digits=20)),
                ('picture', models.ImageField(upload_to='uploads/campaign/')),
                ('date_start', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_end', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Campaigns',
                'ordering': ['name'],
                'permissions': (('can_add_campaign', 'Custom Can add a campaign'), ('can_update_campaigm', 'Custom Can edit a campaign'), ('can_delete_campaign', 'Custom Can delete a campaign')),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=60000)),
                ('picture', models.ImageField(upload_to='uploads/category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
                'permissions': (('can_add_category', 'Custom Can add a Category'), ('can_update_category', 'Custom Can edit a Category'), ('can_delete_category', 'Custom Can delete a Category')),
            },
        ),
        migrations.AddField(
            model_name='campaign',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='campaigns.Category'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]