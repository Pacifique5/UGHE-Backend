from django.core.management import call_command
from django.test import TestCase
from rest_framework.test import APIClient

from content.seed_data import FACTS_TITLE, PREDEFINED_PASSWORD, PREDEFINED_USERNAME


class HomepageApiTests(TestCase):
    def setUp(self):
        call_command("seed_homepage")
        self.client = APIClient()

    def test_homepage_exposes_screenshot_content(self):
        response = self.client.get("/api/homepage/")
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(body["sections"][0]["title"], FACTS_TITLE)
        self.assertEqual(
            [stat["display_value"] for stat in body["sections"][0]["stats"]],
            ["128", "1,260", "677", "4TH"],
        )
        self.assertGreaterEqual(len(body["slides"]), 2)
        self.assertIn("image", {slide["media_type"] for slide in body["slides"]})
        self.assertIn("video", {slide["media_type"] for slide in body["slides"]})
        labels = [item["label"] for item in body["navigation"]]
        self.assertEqual(
            labels,
            [
                "About Us",
                "Academics",
                "Research",
                "Centres and Institutes",
                "Admissions",
                "News and Events",
            ],
        )
        research = next(item for item in body["navigation"] if item["label"] == "Research")
        self.assertEqual(research["children"], [])
        about = next(item for item in body["navigation"] if item["label"] == "About Us")
        self.assertGreaterEqual(len(about["children"]), 1)

    def test_inactive_slide_is_hidden(self):
        from content.models import HeroSlide

        HeroSlide.objects.update(is_active=False)
        response = self.client.get("/api/homepage/")
        self.assertEqual(response.json()["slides"], [])


class LoginApiTests(TestCase):
    def setUp(self):
        call_command("seed_homepage")
        self.client = APIClient()

    def test_predefined_credentials_return_a_token(self):
        response = self.client.post(
            "/api/auth/login/",
            {"username": PREDEFINED_USERNAME, "password": PREDEFINED_PASSWORD},
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()["token"])
        self.assertEqual(response.json()["username"], PREDEFINED_USERNAME)
        self.assertTrue(response.json()["is_staff"])

    def test_wrong_password_is_rejected(self):
        response = self.client.post(
            "/api/auth/login/",
            {"username": PREDEFINED_USERNAME, "password": "not-the-password"},
            format="json",
        )
        self.assertEqual(response.status_code, 400)

    def test_logout_revokes_the_token(self):
        login = self.client.post(
            "/api/auth/login/",
            {"username": PREDEFINED_USERNAME, "password": PREDEFINED_PASSWORD},
            format="json",
        )
        token = login.json()["token"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
        logout = self.client.post("/api/auth/logout/")
        self.assertEqual(logout.status_code, 204)
        me = self.client.get("/api/auth/me/")
        self.assertEqual(me.status_code, 401)
