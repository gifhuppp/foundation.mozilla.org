# Generated by Django 3.1.11 on 2021-06-10 16:55

from django.db import migrations

from wagtail.core.models import BootstrapTranslatableModel

class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0026_add_localization_to_subclasses'),
    ]

    operations = [
        BootstrapTranslatableModel('wagtailpages.Petition'),
        BootstrapTranslatableModel('wagtailpages.Signup'),
    ]
