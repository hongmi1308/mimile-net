import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create or update the default admin user for hosted demos."

    def handle(self, *args, **options):
        username = os.environ.get("ADMIN_USERNAME", "nhatphat")
        password = os.environ.get("ADMIN_PASSWORD", "Admin@12345")
        email = os.environ.get("ADMIN_EMAIL", "nhatphat@example.com")

        User = get_user_model()
        user, created = User.objects.get_or_create(
            username=username,
            defaults={"email": email},
        )
        user.email = user.email or email
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        action = "Created" if created else "Updated"
        self.stdout.write(self.style.SUCCESS(f"{action} admin user: {username}"))
