# SAHARA OIL TRADING S.A. — Application Flask

Version Python du site vitrine : le contenu est piloté par des structures de
données Python, les pages sont rendues par Jinja2, et le formulaire de contact
est réellement traité côté serveur (validation, enregistrement en base,
notification email optionnelle).

## Démarrage rapide

```bash
cd sahara_oil_app
python -m venv .venv
source .venv/bin/activate          # Windows : .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Le site est disponible sur **http://127.0.0.1:5000**.
La base SQLite est créée automatiquement dans `instance/sahara.sqlite`.

## Structure du projet

```
sahara_oil_app/
├── app.py              # Fabrique d'application, routes, configuration
├── content.py          # TOUT le contenu du site (textes, produits, QHSE…)
├── forms.py            # Validation du formulaire de contact
├── db.py               # Persistance SQLite des messages
├── test_app.py         # Suite de tests (11 tests)
├── requirements.txt
├── templates/
│   ├── base.html       # En-tête, navigation, pied de page
│   ├── index.html      # Page d'accueil (toutes les sections)
│   └── 404.html
├── static/
│   ├── css/style.css
│   ├── js/script.js    # Animations + envoi du formulaire vers l'API
│   └── img/            # logo, hero, terminal, pipeline, tanker
└── instance/           # Base de données (créée au premier lancement)
```

## Modifier le contenu

Aucun HTML à toucher : tout se fait dans **`content.py`**.

```python
# Ajouter un produit à la grille « Produits Pétroliers »
PRODUCTS.append({
    "id": "prod-paraffine",
    "icon": "🕯️",
    "name": "Paraffine",
    "description": "Paraffine industrielle et alimentaire, en vrac ou conditionnée.",
    "specs": ["Industrie", "Alimentaire"],
})
```

Il en va de même pour `SERVICES`, `QHSE_PILLARS`, `STATS`, `WHY_CARDS`,
`TICKER_ITEMS`, `CONTACT`, `FOOTER`… La page se met à jour au rechargement.

Les numéros des piliers QHSE (01 → 07) sont calculés automatiquement : ajouter
ou retirer un pilier ne casse pas la numérotation.

## Routes

| Méthode | Route              | Rôle                                              |
|---------|--------------------|---------------------------------------------------|
| GET     | `/`                | Page d'accueil                                    |
| POST    | `/api/contact`     | Réception du formulaire (JSON ou `form-data`)     |
| GET     | `/admin/messages`  | Liste des messages reçus (jeton requis)           |
| GET     | `/healthz`         | Supervision                                       |

### Exemple d'appel à l'API

```bash
curl -X POST http://127.0.0.1:5000/api/contact \
  -H "Content-Type: application/json" \
  -d '{"firstName":"Amina","lastName":"Nkolo","email":"amina@example.cm",
       "service":"distribution","message":"Devis pour 20 000 L de gasoil par mois."}'
```

Réponse en cas de succès (`201`) :

```json
{"ok": true, "id": 1, "message": "Votre message a été envoyé avec succès ! …"}
```

En cas d'erreur (`400`), chaque champ fautif est renvoyé et affiché sous le
champ concerné dans le formulaire :

```json
{"ok": false, "errors": {"email": "Veuillez saisir une adresse email valide."}}
```

## Configuration (variables d'environnement)

| Variable        | Défaut                        | Description                                  |
|-----------------|-------------------------------|----------------------------------------------|
| `SECRET_KEY`    | clé de développement          | **À changer en production**                  |
| `DATABASE`      | `instance/sahara.sqlite`      | Chemin de la base SQLite                     |
| `ADMIN_TOKEN`   | *(vide)*                      | Active `/admin/messages` quand il est défini |
| `HOST` / `PORT` | `127.0.0.1` / `5000`          | Adresse d'écoute                             |
| `FLASK_DEBUG`   | `1`                           | Mettre à `0` en production                   |
| `SMTP_HOST`     | *(vide)*                      | Active la notification email                 |
| `SMTP_PORT`     | `587`                         | Port SMTP                                    |
| `SMTP_USER` / `SMTP_PASSWORD` | *(vide)*        | Identifiants SMTP                            |
| `MAIL_FROM` / `MAIL_TO` | voir `app.py`         | Expéditeur / destinataire des notifications  |

Tant que `SMTP_HOST` n'est pas défini, les messages sont **enregistrés en base**
et la notification email est simplement ignorée (avec une ligne de journal).

## Consulter les messages reçus

```bash
ADMIN_TOKEN="un-jeton-secret" python app.py
curl "http://127.0.0.1:5000/admin/messages?token=un-jeton-secret"
```

Ou directement en SQL :

```bash
sqlite3 instance/sahara.sqlite "SELECT created_at, email, service FROM messages;"
```

## Tests

```bash
python -m unittest test_app -v
```

## Mise en production

```bash
export SECRET_KEY="…" FLASK_DEBUG=0
gunicorn -w 4 -b 0.0.0.0:8000 "app:app"
```

Placer ensuite un reverse proxy (Nginx, Caddy) devant l'application pour le
HTTPS et la mise en cache des fichiers statiques.

## Points d'attention

- Les polices Inter et Playfair Display sont chargées depuis Google Fonts :
  prévoir un hébergement local si le site doit fonctionner hors ligne.
- Le formulaire comporte un champ piège (*honeypot*) invisible contre les
  robots ; pour un trafic important, ajouter une limitation de débit
  (`Flask-Limiter`) sur `/api/contact`.
- Les numéros de téléphone et adresses email de `content.py` sont des
  valeurs d'exemple à remplacer par les coordonnées réelles.
