from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Book


class BookStatusTestCase(TestCase):
    def setUp(self):
        Book.objects.create(
            title='TestBook',
            price=100,
            stock=1,
            publisher=User.objects.create_user(
                username='testuser',
                password='12345',
            )
        )

    def test_book_default_status(self):
        book = Book.objects.get(title='TestBook')
        self.assertEqual(book.is_published(), False)

    def test_book_status_change(self):
        book = Book.objects.get(title='TestBook')
        book.change_status('published')
        self.assertEqual(book.is_published(), True)


class BookViewsTestCase(TestCase):
    def test_main_page_exists_at_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_book_list_exists_at_location(self):
        resp = self.client.get('/book_store/')
        self.assertEqual(resp.status_code, 200)

    def test_book_list_accessible_by_name(self):
        resp = self.client.get(reverse('book_store:book_list'))
        self.assertEqual(resp.status_code, 200)

    def test_book_list_template_is_correct(self):
        resp = self.client.get(reverse('book_store:book_list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'book_store/books/list.html')
