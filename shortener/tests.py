from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import ShortenedURL

class ShortenedURLModelTest(TestCase):
    def test_create_shortened_url(self):
        url = ShortenedURL.objects.create(original_url="https://www.example.com")
        self.assertIsNotNone(url.short_code)
        self.assertEqual(url.original_url, "https://www.example.com")

class ShortenedURLViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_shortened_url(self):
        response = self.client.post('/api/urls/', {'original_url': 'https://www.example.com'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('short_code', response.data)

    def test_retrieve_shortened_url(self):
        url = ShortenedURL.objects.create(original_url="https://www.example.com")
        response = self.client.get(f'/api/urls/{url.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['original_url'], url.original_url)
