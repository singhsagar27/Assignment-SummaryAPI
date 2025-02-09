from django.test import TestCase
from django.contrib.auth.models import User
from unittest.mock import patch
from rest_framework.test import APIClient
from rest_framework import status

class SummaryAPITest(TestCase):
    """
    Unit tests for the summary and bullet points API endpoints using mock authentication.
    """

    def setUp(self):
        """
        Set up test client and mock authentication.
        """
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Mock authentication by forcing the test client to act as an authenticated user
        self.client.force_authenticate(user=self.user)

        self.summary_url = "/api/generate-summary/"
        self.bullet_points_url = "/api/generate-bullet-points/"

    # ✅ 1️⃣ Test Valid API Requests
    @patch("summarizer.views.generate_llm_response", return_value="Mocked summary response.")
    def test_generate_summary_valid_text(self, mock_llm):
        """
        Test generating a summary with valid input.
        """
        response = self.client.post(self.summary_url, {"text": "Django is a Python framework."}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("original_text", response.data)
        self.assertIn("summary", response.data)  # Check for `summary` instead of `result`
        self.assertEqual(response.data["summary"], "Mocked summary response.")

    @patch("summarizer.views.generate_llm_response", return_value="- Bullet 1\n- Bullet 2")
    def test_generate_bullet_points_valid_text(self, mock_llm):
        """
        Test generating bullet points with valid input.
        """
        response = self.client.post(self.bullet_points_url, {"text": "Django simplifies web development."}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("original_text", response.data)
        self.assertIn("bullet_points", response.data)  # Check for `bullet_points`
        self.assertEqual(response.data["bullet_points"], "- Bullet 1\n- Bullet 2")

    # ✅ 2️⃣ Test Invalid Requests
    def test_generate_summary_empty_text(self):
        """
        Test API behavior when an empty text is provided.
        """
        response = self.client.post(self.summary_url, {"text": ""}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"error": "Text is required"})

    def test_generate_bullet_points_empty_text(self):
        """
        Test API behavior when an empty text is provided.
        """
        response = self.client.post(self.bullet_points_url, {"text": ""}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"error": "Text is required"})

    def test_generate_summary_missing_text(self):
        """
        Test API behavior when 'text' key is missing in the request.
        """
        response = self.client.post(self.summary_url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"error": "Text is required"})

    def test_generate_bullet_points_missing_text(self):
        """
        Test API behavior when 'text' key is missing in the request.
        """
        response = self.client.post(self.bullet_points_url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"error": "Text is required"})

    # ✅ 3️⃣ Test Unauthorized Requests
    def test_generate_summary_no_auth(self):
        """
        Test API behavior when authentication is not provided.
        """
        self.client.force_authenticate(user=None)  # Remove authentication
        response = self.client.post(self.summary_url, {"text": "Test input"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_generate_bullet_points_no_auth(self):
        """
        Test API behavior when authentication is not provided.
        """
        self.client.force_authenticate(user=None)  # Remove authentication
        response = self.client.post(self.bullet_points_url, {"text": "Test input"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ✅ 4️⃣ Test Invalid Methods
    def test_generate_summary_invalid_method(self):
        """
        Test accessing the summary endpoint with a GET request instead of POST.
        """
        response = self.client.get(self.summary_url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_generate_bullet_points_invalid_method(self):
        """
        Test accessing the bullet points endpoint with a GET request instead of POST.
        """
        response = self.client.get(self.bullet_points_url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
