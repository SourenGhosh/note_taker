import json
from django.test import TestCase
from django.test import Client

from api_app.models import Note


class NoteTakingTest(TestCase):
    def setUp(self):
        self.client = Client()
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.note_ins = Note.objects.create(title="test-title-123", body="test-body-123")

    @classmethod
    def tearDownClass(cls):
        cls.note_ins.delete()
        super().tearDownClass()

    
    def test_create_note(self):
        response = self.client.post("/notes/", json.dumps({'title':'test', 'body': 'test body'}), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_note_by_title(self):
        response = self.client.get("/notes/?title=test-title-123")
        print(response.json())
        self.assertEqual(response.status_code, 200)