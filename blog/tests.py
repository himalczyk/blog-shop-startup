from django.test import TestCase
from django.utils import timezone
from .models import Post

# Create your tests here.

class PostTests(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title = "Test Post object title",
            description = "Test post object description",
            pub_date = timezone.now(),
            link = "https://micelka.pl",
            image = "https://micelka.pl/logo",
            post_name = "Test post object post name",
            guid = "ea1fd653-984c-4957-b99f-d17fa09a64f7"
        )
        
    def test_post_content(self):
        self.assertEqual(self.post.description, "Test post object description")
        self.assertEqual(self.post.link, "https://micelka.pl")
        self.assertEqual(
            self.post.guid, "ea1fd653-984c-4957-b99f-d17fa09a64f7"
        )
        
    def test_post_str_representation(self):
        self.assertEqual(
            str(self.post), "Test post object post name: Test Post object title"
        )