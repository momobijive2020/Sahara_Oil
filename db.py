"""Couche de persistance (SQLite) pour les messages du formulaire de contact."""

from __future__ import annotations

import sqlite3
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import click
from flask import Flask, current_app, g

SCHEMA = """
CREATE TABLE IF NOT EXISTS messages (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at  TEXT    NOT NULL,
    first_name  TEXT    NOT NULL,
    last_name   TEXT    NOT NULL,
    company     TEXT,
    email       TEXT    NOT NULL,
    phone       TEXT,
    service     TEXT,
    message     TEXT    NOT NULL,
    ip          TEXT,
    user_agent  TEXT
);
CREATE INDEX IF NOT EXISTS idx_messages_created_at ON messages (created_at DESC);
"""


def get_db() -> sqlite3.Connection:
    """Retourne la connexion SQLite liée au contexte de requête courant."""
    if "db" not in g:
        path = Path(current_app.config["DATABASE"])
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            g.db = sqlite3.connect(str(path), detect_types=sqlite3.PARSE_DECLTYPES)
        except (OSError, sqlite3.OperationalError):
            # Système de fichiers en lecture seule (certains hébergeurs) :
            # on bascule sur un emplacement temporaire accessible en écriture.
            fallback = Path(tempfile.gettempdir()) / "sahara.sqlite"
            current_app.logger.warning(
                "Base non accessible à %s — repli sur %s", path, fallback
            )
            g.db = sqlite3.connect(str(fallback), detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def close_db(exception: BaseException | None = None) -> None:
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db() -> None:
    """Crée les tables si elles n'existent pas."""
    get_db().executescript(SCHEMA)
    get_db().commit()


def save_message(data: dict[str, Any], ip: str | None = None,
                 user_agent: str | None = None) -> int:
    """Enregistre un message et retourne son identifiant."""
    db = get_db()
    cursor = db.execute(
        """
        INSERT INTO messages
            (created_at, first_name, last_name, company, email, phone,
             service, message, ip, user_agent)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            datetime.now(timezone.utc).isoformat(timespec="seconds"),
            data["first_name"],
            data["last_name"],
            data.get("company"),
            data["email"],
            data.get("phone"),
            data.get("service"),
            data["message"],
            ip,
            user_agent,
        ),
    )
    db.commit()
    return int(cursor.lastrowid)


def list_messages(limit: int = 50) -> list[dict[str, Any]]:
    """Retourne les derniers messages reçus, du plus récent au plus ancien."""
    rows = get_db().execute(
        "SELECT * FROM messages ORDER BY id DESC LIMIT ?", (limit,)
    ).fetchall()
    return [dict(row) for row in rows]


@click.command("init-db")
def init_db_command() -> None:
    """Commande CLI : flask init-db"""
    init_db()
    click.echo(f"Base de données initialisée : {current_app.config['DATABASE']}")


def init_app(app: Flask) -> None:
    """Branche la gestion de la base sur l'application."""
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    with app.app_context():
        init_db()
