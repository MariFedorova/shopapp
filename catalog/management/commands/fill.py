from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        products_list = [
            {'name': 'персик', 'category': 'фрукт'},
            {'name': 'авокадо', 'category': 'овощ'}
        ]

        products_for_create = []

        for item in products_list:
            products_for_create.append(Category(**item))

        Category.objects.all().delete()
        Category.objects.bulk_create(products_for_create)

