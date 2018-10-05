# Generated by Django 2.1 on 2018-10-01 19:13

from django.db import migrations
from django.db.models.signals import post_save, pre_save
from edc_action_item.site_action_items import site_action_items


def fill_action_item_fk(apps, schema_editor):
    """Re-save instances to update action_item FK.
    """
    post_save.disconnect(dispatch_uid='serialize_on_save')
    pre_save.disconnect(dispatch_uid='requires_consent_on_pre_save')
    app_label = 'edc_locator'
    models = ['subjectlocator']
    for model in models:
        model_cls = apps.get_model(app_label, model)
        for obj in model_cls.objects.all():
            obj.action_name = [
                action.name for action in site_action_items.registry.values()
                if action.reference_model.split('.')[1].lower() == model.lower()][0]
            obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('edc_locator', '0012_auto_20181002_0047'),
        ('edc_action_item', '0012_auto_20181001_2256'),
    ]

    operations = [migrations.RunPython(fill_action_item_fk)]