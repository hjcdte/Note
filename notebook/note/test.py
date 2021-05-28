from datetime import datetime
from django.http import response
from django.contrib.auth.models import User
from rest_framework.test import (
    APIClient,
    APITestCase,
)
from faker import Faker
from django.utils import timezone
from note.models import (
    Note,
    NoteTag,
    NoteAndNoteTag,
    Collections,
)


class NoteModelTests(APITestCase):
    def setUp(self):
        # self.client = APIClient()
        self.user = User.objects.create_user(username="hjc", password="kuaile")
        self.client.force_authenticate(user=self.user)
        self.fake = Faker()
        for i in range(3):
            Note.objects.create(
                title=self.fake.name(),
                content=self.fake.name(),
                datetime=self.fake.date(),
                owner=self.user,
            )

    def test_notes_get(self):
        response = self.client.get("/notes")
        self.assertEqual(response.status_code, 200)

    def test_notes_post(self):
        data = {
            "title": 1,
            "content": 2,
            "datetime": timezone.now(),
            "owner": self.user.id,
        }
        response = self.client.post("/notes", data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_notes_put(self):
        data = {
            "title": 5,
            "content": 2,
            "datetime": timezone.now(),
            "owner": self.user.id,
        }
        id = Note.objects.first().id
        response = self.client.put("/notes/{}".format(id), data, format="json")

        self.assertEqual(response.status_code, 200)

    def test_notes_delete(self):
        id = Note.objects.first().id
        response = self.client.delete("/notes/{}".format(id))
        self.assertEqual(response.status_code, 204)

    def test_notes_str(self):
        note = Note.objects.first()
        note_str = note.title + "-" + note.owner.username
        self.assertEqual(str(note), note_str)

    def tearDown(self):
        Note.objects.all().delete()


class NoteTagModelTests(APITestCase):
    def setUp(self):
        # self.client = APIClient()
        self.user = User.objects.create_user(username="hjc", password="kuaile")
        self.client.force_authenticate(user=self.user)
        self.fake = Faker()
        for i in range(3):
            NoteTag.objects.create(
                title=self.fake.name(),
            )

    def test_tags_get(self):
        response = self.client.get("/tags")
        self.assertEqual(response.status_code, 200)

    def test_tags_post(self):
        data = {
            "title": 'jijijiji',
        }
        response = self.client.post("/tags", data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_tags_put(self):
        data = {
            "title": 'dididiidi',
        }
        id = NoteTag.objects.first().id
        response = self.client.put("/tags/{}".format(id), data, format="json")

        self.assertEqual(response.status_code, 200)

    def test_tags_delete(self):
        id = NoteTag.objects.first().id
        response = self.client.delete("/tags/{}".format(id))
        self.assertEqual(response.status_code, 204)

    def test_tags_str(self):
        note = NoteTag.objects.first()
        self.assertEqual(str(note), note.title)

    def tearDown(self):
        NoteTag.objects.all().delete()


class NoteAndNoteTagModelTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="hjc",
            password="kuaile",
        )
        self.client.force_authenticate(user=self.user)
        self.fake = Faker()

        self.NoteTag = NoteTag.objects.create(
            title=self.fake.name()
        )

        self.Note = Note.objects.create(
            title=self.fake.name(),
            content=self.fake.name(),
            datetime=self.fake.date(),
            owner=self.user,
        )

        self.NoteAndNoteTag = NoteAndNoteTag.objects.create(
            note=self.Note,
            note_tag=self.NoteTag,
        )

    def test_NoteAndNoteTag_get(self):
        response = self.client.get("/tagsAndnotes")
        self.assertEqual(response.status_code, 200)

    def test_NoteAndNoteTag_post(self):
        note = Note.objects.create(
                title=self.fake.name(),
                content=self.fake.name(),
                datetime=self.fake.date(),
                owner=self.user,
            )

        note_tag = NoteTag.objects.create(
                    title=self.fake.name()
            )

        data = {
            "note": note.id,
            "note_tag": note_tag.id
        }

        response = self.client.post("/tagsAndnotes", data)
        self.assertEqual(response.status_code, 201)

    def test_NoteAndNoteTag_str(self):
        NoteAndNoteTag_str = (
            self.NoteAndNoteTag.note_tag.title + "-" + self.NoteAndNoteTag.note.title
        )
        self.assertEqual(str(self.NoteAndNoteTag), NoteAndNoteTag_str)

    def tearDown(self):
        Note.objects.all().delete()
        Collections.objects.all().delete()


class CollectionModelTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="hjc",
            password="kuaile",
        )
        self.client.force_authenticate(user=self.user)
        self.fake = Faker()
        self.notes = list()
        for i in range(3):
            self.notes.append(
                Note.objects.create(
                    title=self.fake.name(),
                    content=self.fake.name(),
                    datetime=self.fake.date(),
                    owner=self.user,
                )
            )

        self.collection = Collections.objects.create(
            owner=self.user,
            note=self.notes[1],
            datetime=self.fake.date(),
        )

    def test_collections_get(self):
        response = self.client.get("/collections")
        self.assertEqual(response.status_code, 200)

    def test_collections_post(self):
        data = {
            "note": self.notes[0].id,
            "datetime": timezone.now(),
            "owner": self.user.id,
        }
        response = self.client.post("/collections", data)
        self.assertEqual(response.status_code, 201)

    def test_collections_str(self):
        collection_str = (
            self.collection.note.title + "-" + self.collection.owner.username
        )
        self.assertEqual(str(self.collection), collection_str)

    def tearDown(self):
        Note.objects.all().delete()
        Collections.objects.all().delete()


# class TokenTests(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username="hjc",
#             password="kuaile",
#         )
#         self.data = {"username": "hjc", "password": "kuaile"}
#
#     def test_token_post(self):
#         response = self.client.post("/api-token-auth/", self.data)
#         self.assertEqual(response.status_code, 200)
#
#     def tearDown(self):
#         Note.objects.all().delete()
#         Collections.objects.all().delete()
