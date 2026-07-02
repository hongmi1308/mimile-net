from django.core.management import call_command
from django.core.management.base import BaseCommand

from app.models import Machine


class Command(BaseCommand):
    help = "Load demo data on hosted databases that do not have machines yet."

    def handle(self, *args, **options):
        if Machine.objects.exists():
            self.stdout.write(self.style.WARNING("Skipped demo data: machines already exist."))
            return

        call_command("loaddata", "render_seed")
        self.stdout.write(self.style.SUCCESS("Loaded render_seed demo data."))
