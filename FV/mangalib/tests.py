from django.test import TestCase
from .models import Author

# Create your tests here.

"""
unitest

"""

class AuthorTestCase(TestCase):
      def setUp(self):
            self.author = Author.objects.create(name="Akira Toriyama")

      def test_author_name(self):
            self.assertEqual(self.author.name, "Akira Toriyama")
            
      def test_author_str(self):
            self.assertEqual(str(self.author), "Akira Toriyama")
            
      

