# Mise en production — SAHARA OIL TRADING

## 1. Versionner le projet avec Git

```bash
cd sahara_oil_app
git init
git add .
git commit -m "Site Sahara Oil Trading — version initiale"
```

Créez un dépôt vide sur GitHub (privé de préférence), puis :

```bash
git remote add origin https://github.com/<votre-compte>/sahara-oil-trading.git
git branch -M main
git push -u origin main
```

Le fichier `.gitignore` exclut déjà `instance/` (base SQLite), `__pycache__/` et `.env`.
**Ne commitez jamais** vos mots de passe : ils passent par des variables
d'environnement (voir §2).

## 2. Variables d'environnement à définir sur le serveur

| Variable | Rôle |
|---|---|
| `SECRET_KEY` | clé secrète Flask (chaîne aléatoire longue) |
| `ADMIN_TOKEN` | jeton pour consulter `/admin/messages` |
| `SMTP_PASSWORD` | **seule variable mail obligatoire** : mot de passe de la boîte IONOS `saharaoil.trading@saharaoiltrading.org` |
| `FLASK_DEBUG` | `0` en production |

Messagerie IONOS pré-configurée dans `app.py` (`smtp.ionos.fr`, port 587, TLS,
expéditeur et destinataire `saharaoil.trading@saharaoiltrading.org`) — voir `.env.example`.
Ajoutez le SPF IONOS au DNS : `v=spf1 include:_spf.perfora.net include:_spf.kundenserver.de ~all`, et activez DKIM.

## 3. Déploiement (option A — Render / Railway, le plus simple)

1. « New Web Service » → connectez le dépôt GitHub.
2. Build : `pip install -r requirements.txt`
3. Start : `gunicorn app:app --bind 0.0.0.0:$PORT`
4. Ajoutez les variables d'environnement du §2.
5. Ajoutez le domaine `saharaoiltrading.org` (CNAME fourni par la plateforme).

Chaque `git push` sur `main` redéploie automatiquement.

## 4. Déploiement (option B — VPS + Docker)

```bash
git clone https://github.com/<votre-compte>/sahara-oil-trading.git
cd sahara-oil-trading
docker build -t sahara-oil .
docker run -d --name sahara -p 8000:8000 --env-file .env \
  -v /srv/sahara/instance:/app/instance sahara-oil
```

Puis Nginx en reverse proxy devant le port 8000 et HTTPS via
`certbot --nginx -d saharaoiltrading.org -d www.saharaoiltrading.org`.

Mise à jour : `git pull && docker build -t sahara-oil . && docker restart sahara`.

## 5. Vérifications après mise en ligne

- `https://saharaoiltrading.org/healthz` renvoie `{"status":"ok"}`
- le formulaire de contact enregistre et notifie par e-mail
- le bouton **EN / FR** de la barre de navigation traduit la page
- HTTPS actif, `FLASK_DEBUG=0`
