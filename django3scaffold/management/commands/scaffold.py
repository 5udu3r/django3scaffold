from __future__ import absolute_import
from __future__ import print_function
from django.core.management.base import BaseCommand

from optparse import make_option

from django3scaffold.scaffold import Scaffold
from django3scaffold import settings


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('app')

        parser.add_argument('--model', default=None, dest='model', nargs='+', metavar='N',)

    def handle(self, *args, **options):

        app = options['app']
        model = options['model'][0]
        myargs = options['model'][1:]
        if len(app) == 0:
            print("You must provide app name. For example:\n\npython manage.py scallfold my_app\n")
            return
        # import ipdb
        # ipdb.set_trace()
        scaffold = Scaffold(app, model, myargs)
        scaffold.run()
        self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % app))

    def get_version(self):
        return 'django-common version: %s' % settings.VERSION


