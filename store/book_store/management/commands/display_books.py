from django.core.management.base import BaseCommand
from ...models import Book


class Command(BaseCommand):
    help = (
        'Displays list of books with possibility to order by publish date '
        'ordering (asc/desc)'
    )

    def add_arguments(self, parser):
        parser.add_argument(
            '--order',
            dest='order',
            default='asc',
            type=str,
            help=(
                'sets the printing order, asc is by default \n '
                'usage: --order desc'
            )
        )
        parser.add_argument(
            '--limit',
            dest='limit',
            default=10,
            type=int,
            help=(
                'sets the limit of objects to query, 10 is default \n '
                'usage: --limit 100'
            )
        )

    def handle(self, *args, **options):
        books = Book.objects
        if options['order'] == 'asc':
            books = books.order_by('publish_date')[:int(options['limit'])]
        elif options['order'] == 'desc':
            books = books.order_by('-publish_date')[:int(options['limit'])]
        else:
            books = books.all()[:int(options['limit'])]
        for book in books:
            self.stdout.write(f'{book.id}, {book.title}, {book.publish_date}')
