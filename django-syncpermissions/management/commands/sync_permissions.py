# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand
from django.db.models import get_models, get_app
from django.contrib.auth.management import create_permissions
from django.apps import apps

class Command(BaseCommand):
    args = '<app app ...>'
    help = 'Sync permissions for specified apps, or all apps if none specified'

    def handle(self, *args, **options):
        _apps = []

        if not args:
            for model in get_models():
                _apps.append(apps.get_app_config(model._meta.app_label))
        else:
            for arg in args:
                _apps.append(apps.get_app_config(arg))

        for app in _apps:
            create_permissions(app, get_models(), options.get('verbosity', 0))
