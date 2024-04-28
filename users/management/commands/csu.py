from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Класс для создания суперюзера"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email='sergo.@gmail.com',
            first_name='Test',
            last_name='test',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('sergo1613')
        user.save()
