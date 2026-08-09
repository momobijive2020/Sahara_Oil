"""Tests de l'application — exécuter avec :  python -m unittest test_app -v"""

import tempfile
import unittest
from pathlib import Path

from app import Config, create_app
import db


class SaharaAppTestCase(unittest.TestCase):

    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()

        class TestConfig(Config):
            TESTING = True
            DATABASE = str(Path(self.tmpdir.name) / "test.sqlite")
            SMTP_HOST = None
            ADMIN_TOKEN = "jeton-de-test"

        self.app = create_app(TestConfig)
        self.client = self.app.test_client()

    def tearDown(self):
        self.tmpdir.cleanup()

    # ---- Page d'accueil ----

    def test_homepage_renders(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        body = response.get_data(as_text=True)
        self.assertIn("SAHARA OIL TRADING", body)
        self.assertIn("Politique", body)
        self.assertIn("Jet A-1", body)          # produit issu de content.py
        self.assertIn("Amélioration Continue", body)  # 7e pilier QHSE

    def test_static_assets_served(self):
        for path in ("/static/css/style.css", "/static/js/script.js",
                     "/static/img/logo.jpg"):
            with self.subTest(path=path):
                self.assertEqual(self.client.get(path).status_code, 200)

    def test_healthcheck(self):
        response = self.client.get("/healthz")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "ok")

    def test_unknown_page_returns_404(self):
        self.assertEqual(self.client.get("/page-inexistante").status_code, 404)

    # ---- Formulaire de contact ----

    def test_valid_submission_is_saved(self):
        response = self.client.post("/api/contact", json={
            "firstName": "Amina",
            "lastName": "Nkolo",
            "company": "Transports du Littoral",
            "email": "amina@example.cm",
            "phone": "+237 690 00 00 00",
            "service": "distribution",
            "message": "Nous souhaitons un devis pour 20 000 litres de gasoil par mois.",
        })
        self.assertEqual(response.status_code, 201)
        payload = response.get_json()
        self.assertTrue(payload["ok"])
        self.assertIsInstance(payload["id"], int)

        with self.app.app_context():
            messages = db.list_messages()
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0]["email"], "amina@example.cm")

    def test_missing_required_fields_rejected(self):
        response = self.client.post("/api/contact", json={"email": ""})
        self.assertEqual(response.status_code, 400)
        errors = response.get_json()["errors"]
        for field in ("firstName", "lastName", "email", "message"):
            self.assertIn(field, errors)

    def test_invalid_email_rejected(self):
        response = self.client.post("/api/contact", json={
            "firstName": "Jean", "lastName": "Mbarga",
            "email": "pas-un-email",
            "message": "Bonjour, je souhaite des informations tarifaires.",
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("email", response.get_json()["errors"])

    def test_unknown_service_rejected(self):
        response = self.client.post("/api/contact", json={
            "firstName": "Jean", "lastName": "Mbarga",
            "email": "jean@example.cm", "service": "inconnu",
            "message": "Bonjour, je souhaite des informations tarifaires.",
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("service", response.get_json()["errors"])

    def test_honeypot_blocks_bots(self):
        response = self.client.post("/api/contact", json={
            "firstName": "Bot", "lastName": "Spam",
            "email": "bot@example.com", "website": "http://spam.example",
            "message": "Message automatique de spam publicitaire.",
        })
        self.assertEqual(response.status_code, 400)

    def test_form_encoded_submission_also_works(self):
        response = self.client.post("/api/contact", data={
            "firstName": "Paul", "lastName": "Etoga",
            "email": "paul@example.cm",
            "message": "Demande de partenariat pour la région de l'Est.",
        })
        self.assertEqual(response.status_code, 201)

    # ---- Administration ----

    def test_admin_requires_token(self):
        self.assertEqual(self.client.get("/admin/messages").status_code, 403)
        response = self.client.get("/admin/messages?token=jeton-de-test")
        self.assertEqual(response.status_code, 200)
        self.assertIn("messages", response.get_json())


if __name__ == "__main__":
    unittest.main(verbosity=2)
