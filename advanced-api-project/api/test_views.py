from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from api.models import Author, Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        # Create author
        self.author = Author.objects.create(name="Chinua Achebe")

        # Create book
        self.book = Book.objects.create(
            title="Things Fall Apart",
            publication_year=1958,
            author=self.author
        )

        # API URLs
        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book.id}/"
        self.create_url = "/api/books/create/"
        self.update_url = f"/api/books/update/{self.book.id}/"
        self.delete_url = f"/api/books/delete/{self.book.id}/"

    # -----------------------------
    # READ (List)
    # -----------------------------
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # -----------------------------
    # READ (Detail)
    # -----------------------------
    def test_retrieve_single_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Things Fall Apart")

    # -----------------------------
    # CREATE (Authenticated)
    # -----------------------------
    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "Arrow of God",
            "publication_year": 1964,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    # -----------------------------
    # CREATE (Unauthenticated)
    # -----------------------------
    def test_create_book_unauthenticated(self):
        data = {
            "title": "No Longer at Ease",
            "publication_year": 1960,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # -----------------------------
    # UPDATE
    # -----------------------------
    def test_update_book(self):
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "Things Fall Apart (Updated)",
            "publication_year": 1958,
            "author": self.author.id
        }

        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Things Fall Apart (Updated)")

    # -----------------------------
    # DELETE
    # -----------------------------
    def test_delete_book(self):
        self.client.login(username="testuser", password="testpassword")

        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

