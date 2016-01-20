# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand
from django.apps import apps as a
from django.contrib.auth.management import create_permissions

class Command(BaseCommand):
    args = '<app app ...>'
    help = 'Sync permissions for specified apps, or all apps if none specified'

    def handle(self, *args, **options):
        if not args:
            apps = []
            for model in a.get_models():
                apps.append(a.get_app_config(model._meta.app_label))
        else:
            apps = []
            for arg in args:
                apps.append(a.get_app_config(arg))
        for app in apps:
            create_permissions(app, a.get_models(), options.get('verbosity', 0))
