# Generated by Django 2.2.2 on 2019-06-26 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edc_locator', '0018_auto_20190305_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalsubjectlocator',
            name='action_item_reason',
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='subjectlocator',
            name='action_item_reason',
            field=models.TextField(editable=False, null=True),
        ),
    ]
