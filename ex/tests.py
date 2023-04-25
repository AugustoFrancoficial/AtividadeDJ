from django.test import TestCase
from django.urls import reverse


class MyViewTestCase(TestCase):
    def test_my_view(self):
        response = self.client.get(reverse('my_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Texto que deve estar na página")
