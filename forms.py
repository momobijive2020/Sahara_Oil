"""Validation côté serveur du formulaire de contact.

Aucune dépendance externe : validation explicite, messages en français,
retournés au format attendu par le front-end (dict champ -> message).
"""

from __future__ import annotations

import re
from typing import Any

from content import SERVICE_CHOICES

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s.]+(\.[^@\s.]+)+$")
PHONE_RE = re.compile(r"^[+()\d\s.\-]{6,25}$")

MAX_LENGTHS = {
    "first_name": 80,
    "last_name": 80,
    "company": 120,
    "email": 160,
    "phone": 25,
    "message": 4000,
}


def _clean(value: Any) -> str:
    """Normalise une valeur brute en chaîne nettoyée."""
    if value is None:
        return ""
    return " ".join(str(value).split()) if not isinstance(value, str) else str(value).strip()


def validate_contact(payload: dict[str, Any]) -> tuple[dict[str, str], dict[str, str]]:
    """Valide les données du formulaire.

    Retourne un tuple ``(data, errors)``.
    - ``data``   : les champs nettoyés, prêts à être enregistrés.
    - ``errors`` : dictionnaire ``champ -> message``, vide si tout est valide.
    """
    data: dict[str, str] = {
        "first_name": _clean(payload.get("firstName") or payload.get("first_name")),
        "last_name": _clean(payload.get("lastName") or payload.get("last_name")),
        "company": _clean(payload.get("company")),
        "email": _clean(payload.get("email")).lower(),
        "phone": _clean(payload.get("phone")),
        "service": _clean(payload.get("service")),
        "message": _clean(payload.get("message")),
    }
    errors: dict[str, str] = {}

    if not data["first_name"]:
        errors["firstName"] = "Le prénom est obligatoire."
    if not data["last_name"]:
        errors["lastName"] = "Le nom est obligatoire."

    if not data["email"]:
        errors["email"] = "L'email est obligatoire."
    elif not EMAIL_RE.match(data["email"]):
        errors["email"] = "Veuillez saisir une adresse email valide."

    if data["phone"] and not PHONE_RE.match(data["phone"]):
        errors["phone"] = "Le numéro de téléphone n'est pas valide."

    if data["service"] and data["service"] not in SERVICE_CHOICES:
        errors["service"] = "Type de service inconnu."

    if not data["message"]:
        errors["message"] = "Le message est obligatoire."
    elif len(data["message"]) < 10:
        errors["message"] = "Merci de détailler votre besoin (10 caractères minimum)."

    for field, maximum in MAX_LENGTHS.items():
        key = {"first_name": "firstName", "last_name": "lastName"}.get(field, field)
        if len(data[field]) > maximum:
            errors[key] = f"Ce champ ne peut dépasser {maximum} caractères."

    # Piège à robots : champ caché qui doit rester vide.
    if _clean(payload.get("website")):
        errors["website"] = "Requête rejetée."

    return data, errors
