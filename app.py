"""
SAHARA OIL TRADING S.A. — Application web Flask.

Lancement rapide :
    pip install -r requirements.txt
    python app.py

L'application est ensuite disponible sur http://127.0.0.1:5000
"""

from __future__ import annotations

import logging
import os
import smtplib
from email.message import EmailMessage
from pathlib import Path

from flask import (
    Flask,
    abort,
    jsonify,
    render_template,
    request,
)

import content
import db
from forms import validate_contact

BASE_DIR = Path(__file__).resolve().parent

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger("sahara")


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------


class Config:
    """Configuration par défaut, surchargeable par variables d'environnement."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-key-a-changer-en-production")
    DATABASE = os.environ.get("DATABASE", str(BASE_DIR / "instance" / "sahara.sqlite"))

    # Jeton protégeant la consultation des messages reçus (/admin/messages).
    ADMIN_TOKEN = os.environ.get("ADMIN_TOKEN")

    # Notification email — désactivée tant que SMTP_HOST n'est pas défini.
    # Messagerie IONOS de SAHARA OIL TRADING pré-configurée.
    # Seul SMTP_PASSWORD doit être fourni par variable d'environnement.
    SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.ionos.fr")
    SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
    SMTP_USER = os.environ.get("SMTP_USER", "saharaoil.trading@saharaoiltrading.org")
    SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
    SMTP_USE_TLS = os.environ.get("SMTP_USE_TLS", "1") == "1"
    MAIL_FROM = os.environ.get("MAIL_FROM", "saharaoil.trading@saharaoiltrading.org")
    MAIL_TO = os.environ.get("MAIL_TO", content.CONTACT["email"])


# ---------------------------------------------------------------------------
# Notification email (optionnelle)
# ---------------------------------------------------------------------------


def send_notification(app: Flask, data: dict[str, str], message_id: int) -> None:
    """Envoie un email de notification si le SMTP est configuré.

    Une erreur d'envoi n'invalide jamais l'enregistrement du message :
    elle est journalisée puis ignorée.
    """
    if not app.config["SMTP_HOST"] or not app.config["SMTP_PASSWORD"]:
        logger.info(
            "SMTP_PASSWORD absent — notification email ignorée (message #%s). "
            "Le message reste enregistré en base.",
            message_id,
        )
        return

    service = content.SERVICE_CHOICES.get(data.get("service", ""), "Non précisé")
    mail = EmailMessage()
    mail["Subject"] = f"[Site web] Nouveau message #{message_id} — {data['last_name']}"
    mail["From"] = app.config["MAIL_FROM"]
    recipients = [r.strip() for r in str(app.config["MAIL_TO"]).replace(";", ",").split(",") if r.strip()]
    mail["To"] = ", ".join(recipients)
    mail["Reply-To"] = data["email"]
    mail.set_content(
        f"Nouveau message reçu via le site web\n"
        f"{'-' * 45}\n"
        f"Nom        : {data['first_name']} {data['last_name']}\n"
        f"Entreprise : {data.get('company') or '—'}\n"
        f"Email      : {data['email']}\n"
        f"Téléphone  : {data.get('phone') or '—'}\n"
        f"Service    : {service}\n"
        f"{'-' * 45}\n\n"
        f"{data['message']}\n"
    )

    try:
        with smtplib.SMTP(app.config["SMTP_HOST"], app.config["SMTP_PORT"], timeout=15) as smtp:
            if app.config["SMTP_USE_TLS"]:
                smtp.starttls()
            if app.config["SMTP_USER"]:
                smtp.login(app.config["SMTP_USER"], app.config["SMTP_PASSWORD"])
            smtp.send_message(mail)
        logger.info("Notification envoyée pour le message #%s.", message_id)
    except Exception as exc:  # noqa: BLE001 — on ne bloque jamais l'utilisateur
        logger.error("Échec de l'envoi de la notification (#%s) : %s", message_id, exc)


# ---------------------------------------------------------------------------
# Fabrique d'application
# ---------------------------------------------------------------------------


def create_app(config_object: type[Config] = Config) -> Flask:
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_object)

    db.init_app(app)

    # ---- Contexte global des templates ----
    @app.context_processor
    def inject_content() -> dict:
        return {
            "site": content.SITE,
            "contact": content.CONTACT,
            "nav_links": content.NAV_LINKS,
            "hero": content.HERO,
            "ticker_items": content.TICKER_ITEMS,
            "about": content.ABOUT,
            "services": content.SERVICES,
            "products": content.PRODUCTS,
            "stats": content.STATS,
            "qhse_intro": content.QHSE_INTRO,
            "qhse_pillars": content.QHSE_PILLARS,
            "qhse_cta": content.QHSE_CTA,
            "why_cards": content.WHY_CARDS,
            "contact_items": content.CONTACT_ITEMS,
            "markets": content.MARKETS,
            "service_choices": content.SERVICE_CHOICES,
            "footer": content.FOOTER,
            "social_links": content.SOCIAL_LINKS,
        }

    # ---- Pages ----
    @app.get("/")
    def index():
        return render_template("index.html")

    # ---- API : formulaire de contact ----
    @app.post("/api/contact")
    def api_contact():
        payload = request.get_json(silent=True) or request.form.to_dict()
        data, errors = validate_contact(payload)

        if errors:
            return jsonify({"ok": False, "errors": errors}), 400

        message_id = 0
        try:
            message_id = db.save_message(
                data,
                ip=request.headers.get("X-Forwarded-For", request.remote_addr),
                user_agent=request.headers.get("User-Agent"),
            )
            logger.info("Message #%s enregistré (%s).", message_id, data["email"])
        except Exception:  # noqa: BLE001 — base indisponible : on notifie quand même
            logger.exception("Enregistrement en base impossible — envoi de l'email malgré tout.")

        try:
            send_notification(app, data, message_id)
        except Exception:  # noqa: BLE001
            logger.exception("Notification email impossible (message #%s).", message_id)

        return jsonify({
            "ok": True,
            "id": message_id,
            "message": (
                "Votre message a été envoyé avec succès ! "
                "Notre équipe vous contactera sous 24h."
            ),
        }), 201

    # ---- Consultation des messages (protégée par jeton) ----
    @app.get("/admin/messages")
    def admin_messages():
        token = app.config["ADMIN_TOKEN"]
        if not token:
            abort(404)
        provided = request.headers.get("X-Admin-Token") or request.args.get("token")
        if provided != token:
            abort(403)
        return jsonify({"messages": db.list_messages(limit=200)})

    # ---- Supervision ----
    @app.get("/healthz")
    def healthz():
        return jsonify({"status": "ok", "service": "sahara-oil-trading"})

    # ---- Erreurs ----
    @app.errorhandler(404)
    def not_found(_error):
        if request.path.startswith(("/api/", "/admin/")):
            return jsonify({"ok": False, "error": "Ressource introuvable."}), 404
        return render_template("404.html"), 404

    @app.errorhandler(Exception)
    def unhandled_error(error):
        from werkzeug.exceptions import HTTPException

        if isinstance(error, HTTPException):
            return error
        logger.exception("Exception non gérée : %s", error)
        if request.path.startswith(("/api/", "/admin/")):
            return jsonify({"ok": False, "error": "Erreur interne du serveur."}), 500
        return jsonify({"ok": False, "error": "Erreur interne du serveur."}), 500

    @app.errorhandler(500)
    def server_error(error):
        logger.exception("Erreur serveur : %s", error)
        return jsonify({"ok": False, "error": "Erreur interne du serveur."}), 500

    return app


app = create_app()


if __name__ == "__main__":
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "1") == "1"
    logger.info("SAHARA OIL TRADING — démarrage sur http://%s:%s", host, port)
    app.run(host=host, port=port, debug=debug)
