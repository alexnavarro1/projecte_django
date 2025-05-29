from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Developer, Genre, Game
from datetime import date

class ModelsTest(TestCase):
    def setUp(self):
        self.dev = Developer.objects.create(name="Epic Games")
        self.genre = Genre.objects.create(name="Shooter")

        image_content = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xFF\xFF\xFF\x21\xF9\x04\x01\x00\x00\x00\x00\x2C\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4C\x01\x00\x3B'
        image_file = SimpleUploadedFile("test_image.gif", image_content, content_type="image/gif")

        self.game = Game.objects.create(
            title="Fortnite",
            description="Battle Royale Game",
            price=0.00,
            release_date=date(2017, 7, 21),
            developer=self.dev,
            image=image_file,  
        )
        self.game.genres.add(self.genre)

    def test_developer_str_and_slug(self):
        self.assertEqual(str(self.dev), "Epic Games")
        self.assertEqual(self.dev.slug, "epic-games")

    def test_genre_str_and_slug(self):
        self.assertEqual(str(self.genre), "Shooter")
        self.assertEqual(self.genre.slug, "shooter")

    def test_game_str_and_slug(self):
        self.assertEqual(str(self.game), "Fortnite")
        self.assertEqual(self.game.slug, "fortnite")

    def test_game_developer_relation(self):
        self.assertEqual(self.game.developer, self.dev)

    def test_game_genre_relation(self):
        self.assertIn(self.genre, self.game.genres.all())

class ViewsTest(TestCase):
    def setUp(self):
        self.dev = Developer.objects.create(name="Epic Games")
        self.genre = Genre.objects.create(name="Shooter")

        image_content = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xFF\xFF\xFF\x21\xF9\x04\x01\x00\x00\x00\x00\x2C\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4C\x01\x00\x3B'
        image_file = SimpleUploadedFile("test_image.gif", image_content, content_type="image/gif")

        self.game = Game.objects.create(
            title="Fortnite",
            description="Battle Royale Game",
            price=0.00,
            release_date=date(2017, 7, 21),
            developer=self.dev,
            image=image_file,  
        )
        self.game.genres.add(self.genre)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Fortnite")

    def test_game_list_view(self):
        response = self.client.get(reverse('games-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.game.title)

    def test_game_detail_view(self):
        response = self.client.get(reverse('games-detail', args=[self.game.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.game.description)

    def test_developer_list_view(self):
        response = self.client.get(reverse('developers-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.dev.name)

    def test_developer_detail_view(self):
        response = self.client.get(reverse('developers-detail', args=[self.dev.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.dev.bio or "")

    def test_genre_list_view(self):
        response = self.client.get(reverse('genres-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.genre.name)

    def test_genre_game_list_view(self):
        response = self.client.get(reverse('genre-games', args=[self.genre.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.game.title)

    def test_404_view(self):
        response = self.client.get(reverse('test-404'))
        self.assertEqual(response.status_code, 404)
