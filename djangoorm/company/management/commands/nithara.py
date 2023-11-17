from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Displays nithara'

    def handle(self,*args, **kwargs):
        self.stdout.write("She is my gem")
