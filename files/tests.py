from files.models import ControlFile
from django.test import TestCase
from django.urls import reverse
from django.core import management

# Create your tests here.


class FileTests(TestCase):
    def setUp(self):
        management.call_command("extract_data", "recaudos.txt")

    def test_file_url_exists(self):
        file = ControlFile.objects.first()
        resp = self.client.get(reverse("files:detail", kwargs={"id_": file.id}))
        self.assertEqual(resp.status_code, 200)

    def test_file_not_found(self):
        resp = self.client.get(reverse("files:detail", kwargs={"id_": 0}))
        self.assertEqual(resp.status_code, 404)
