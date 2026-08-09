"""
SAHARA OIL TRADING S.A. — Contenu du site.

Tout le contenu éditorial est centralisé ici sous forme de structures Python.
Pour modifier le site, il suffit d'éditer ce fichier : les templates Jinja2
bouclent automatiquement sur ces données.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Identité de la société
# ---------------------------------------------------------------------------

SITE = {
    "name": "SAHARA OIL TRADING",
    "legal_form": "S.A.",
    "tagline": "S.A. — Cameroun",
    "title": (
        "SAHARA OIL TRADING S.A. – Distribution & Commerce de Produits "
        "Pétroliers au Cameroun"
    ),
    "description": (
        "SAHARA OIL TRADING S.A. est une société camerounaise leader dans la "
        "distribution, l'importation et l'exportation de produits pétroliers. "
        "Fiabilité, excellence et expertise énergétique en Afrique Centrale."
    ),
    "keywords": (
        "pétrole Cameroun, produits pétroliers, importation exportation huile, "
        "carburant Cameroun, SAHARA OIL TRADING"
    ),
    "og_description": (
        "Spécialiste en distribution, importation et exportation de produits "
        "pétroliers au Cameroun."
    ),
    "copyright_year": 2024,
}

CONTACT = {
    "city": "Yaoundé, Cameroun",
    "region": "Afrique Centrale",
    "phone": "+237 000 000 000",
    "hours": "Lun–Ven: 08h00 – 18h00",
    "email": "contact@saharaoiltrading.cm",
    "email_secondary": "info@saharaoiltrading.cm",
    "port": "Port de Douala, Cameroun",
    "port_detail": "Terminal Pétrolier",
}

# ---------------------------------------------------------------------------
# Navigation
# ---------------------------------------------------------------------------

NAV_LINKS = [
    {"id": "accueil", "label": "Accueil"},
    {"id": "apropos", "label": "À Propos"},
    {"id": "services", "label": "Services"},
    {"id": "produits", "label": "Produits"},
    {"id": "qhse", "label": "Politique QHSE-E"},
    {"id": "chiffres", "label": "Chiffres Clés"},
    {"id": "contact", "label": "Contact"},
]

# ---------------------------------------------------------------------------
# Hero
# ---------------------------------------------------------------------------

HERO = {
    "badge": "Entreprise Camerounaise de Confiance",
    "title_sub": "L'Excellence au Service",
    "title_main": "de l'Énergie",
    "title_accent": "Africaine",
    "description": (
        "SAHARA OIL TRADING S.A. est votre partenaire stratégique pour la "
        "distribution, l'importation et l'exportation de produits pétroliers en "
        "Afrique Centrale. Fiabilité, sécurité et excellence opérationnelle."
    ),
    "stats": [
        {"number": "15+", "label": "Années d'Expérience"},
        {"number": "50+", "label": "Partenaires Actifs"},
        {"number": "10+", "label": "Pays Desservis"},
    ],
}

TICKER_ITEMS = [
    "🛢️ Distribution de carburant au Cameroun",
    "⚡ Approvisionnement fiable en produits pétroliers",
    "🌍 Exportation vers l'Afrique Centrale et de l'Ouest",
    "🚢 Importation internationale de pétrole brut",
    "🏆 Certification ISO & conformité internationale",
    "📊 Marchés: Yaoundé · Douala · Libreville · N'Djamena · Bangui",
]

# ---------------------------------------------------------------------------
# À propos
# ---------------------------------------------------------------------------

ABOUT = {
    "badge": "À Propos de Nous",
    "title": "Un Pilier Énergétique",
    "title_accent": "au Cœur de l'Afrique",
    "lead": (
        "Fondée au Cameroun, <strong>SAHARA OIL TRADING S.A.</strong> s'est "
        "imposée comme un acteur majeur du secteur des hydrocarbures en "
        "Afrique Centrale."
    ),
    "paragraphs": [
        "Notre société allie expertise locale et standards internationaux pour "
        "offrir des solutions énergétiques complètes et fiables. De "
        "l'importation à la distribution finale, nous maîtrisons toute la "
        "chaîne de valeur des produits pétroliers.",
        "Avec une équipe de professionnels chevronnés et une infrastructure "
        "logistique de pointe, nous garantissons des approvisionnements "
        "continus, sécurisés et conformes aux normes environnementales les "
        "plus strictes.",
    ],
    "floating_card": {
        "icon": "🏆",
        "title": "Leader Régional",
        "subtitle": "Afrique Centrale & de l'Ouest",
    },
    "features": [
        {
            "icon": "✅",
            "title": "Conformité Réglementaire",
            "text": "Respect des normes camerounaises et internationales",
        },
        {
            "icon": "🔒",
            "title": "Sécurité & Fiabilité",
            "text": "Processus certifiés et infrastructure sécurisée",
        },
        {
            "icon": "🌐",
            "title": "Réseau International",
            "text": "Partenariats solides avec fournisseurs mondiaux",
        },
    ],
}

# ---------------------------------------------------------------------------
# Services
# ---------------------------------------------------------------------------

_SVG_DISTRIBUTION = """
<svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="32" cy="32" r="30" stroke="currentColor" stroke-width="2"/>
  <path d="M20 32h24M32 20v24" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>
  <circle cx="32" cy="32" r="6" fill="currentColor" opacity="0.3"/>
</svg>
"""

_SVG_IMPORT = """
<svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M8 44l8-16 10 8 8-20 10 12 10-8" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M12 52h40" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
</svg>
"""

_SVG_EXPORT = """
<svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M32 12v28M20 28l12 12 12-12" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M16 44h32" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
  <circle cx="32" cy="52" r="3" fill="currentColor"/>
</svg>
"""

SERVICES = [
    {
        "id": "service-distribution",
        "link_id": "service-dist-link",
        "featured": False,
        "image": "distribution_terminal.jpg",
        "image_alt": "Distribution pétrolière",
        "icon_svg": _SVG_DISTRIBUTION,
        "title": "Distribution Locale",
        "description": (
            "Approvisionnement fiable en carburant, lubrifiants et produits "
            "dérivés sur l'ensemble du territoire camerounais. Réseau de "
            "distribution dense avec flotte logistique moderne."
        ),
        "items": [
            "Gasoil & Essence",
            "Lubrifiants industriels",
            "Bitume & Asphalte",
            "GPL (Gaz de pétrole liquéfié)",
        ],
    },
    {
        "id": "service-import",
        "link_id": "service-import-link",
        "featured": True,
        "featured_label": "⭐ Service Phare",
        "image": "tanker_ship.jpg",
        "image_alt": "Importation pétrolière",
        "icon_svg": _SVG_IMPORT,
        "title": "Importation",
        "description": (
            "Sourcing et importation de pétrole brut et produits raffinés "
            "depuis les marchés internationaux. Conformité douanière assurée "
            "et délais optimisés grâce à notre réseau de partenaires "
            "stratégiques."
        ),
        "items": [
            "Pétrole brut (Crude Oil)",
            "Produits raffinés",
            "Conformité douanière",
            "Gestion des risques",
        ],
    },
    {
        "id": "service-export",
        "link_id": "service-export-link",
        "featured": False,
        "image": "pipeline_export.jpg",
        "image_alt": "Exportation pétrolière",
        "icon_svg": _SVG_EXPORT,
        "title": "Exportation",
        "description": (
            "Exportation vers les pays d'Afrique Centrale et de l'Ouest. "
            "Solutions logistiques complètes incluant transport maritime, "
            "ferroviaire et routier. Documentation internationale maîtrisée."
        ),
        "items": [
            "Afrique Centrale & Ouest",
            "Transport multimodal",
            "Documentation internationale",
            "Assurance & traçabilité",
        ],
    },
]

# ---------------------------------------------------------------------------
# Produits
# ---------------------------------------------------------------------------

PRODUCTS = [
    {
        "id": "prod-gasoil",
        "icon": "⛽",
        "name": "Gasoil / Diesel",
        "description": (
            "Carburant haute performance pour transport, industrie et "
            "agriculture. Conforme aux normes EU."
        ),
        "specs": ["Transport", "Industrie", "Agriculture"],
    },
    {
        "id": "prod-essence",
        "icon": "🔥",
        "name": "Essence Super",
        "description": (
            "Essence sans plomb premium pour véhicules légers et motocycles. "
            "Qualité certifiée."
        ),
        "specs": ["Automobile", "Premium"],
    },
    {
        "id": "prod-fuel",
        "icon": "🏭",
        "name": "Fuel Oil",
        "description": (
            "Combustible lourd pour installations industrielles, centrales "
            "thermiques et bateaux."
        ),
        "specs": ["Industrie lourde", "Maritime"],
    },
    {
        "id": "prod-jet",
        "icon": "✈️",
        "name": "Jet A-1 (Kérosène)",
        "description": (
            "Carburant aviation de haute pureté pour compagnies aériennes et "
            "aéroports."
        ),
        "specs": ["Aviation", "Haute Pureté"],
    },
    {
        "id": "prod-lubrifiant",
        "icon": "🛢️",
        "name": "Lubrifiants",
        "description": (
            "Gamme complète d'huiles moteurs, graisses industrielles et "
            "fluides hydrauliques."
        ),
        "specs": ["Moteurs", "Hydraulique", "Industriel"],
    },
    {
        "id": "prod-gpl",
        "icon": "💨",
        "name": "GPL / Butane",
        "description": (
            "Gaz de pétrole liquéfié pour usage domestique et industriel. "
            "Bouteilles et vrac."
        ),
        "specs": ["Domestique", "Vrac"],
    },
    {
        "id": "prod-bitume",
        "icon": "🏗️",
        "name": "Bitume",
        "description": (
            "Bitume routier et industriel pour construction d'infrastructures "
            "et revêtement."
        ),
        "specs": ["BTP", "Routier"],
    },
    {
        "id": "prod-brut",
        "icon": "🌊",
        "name": "Pétrole Brut",
        "description": (
            "Pétrole brut léger et lourd pour raffineries et trading "
            "international."
        ),
        "specs": ["Trading", "Raffinage", "International"],
    },
]

# ---------------------------------------------------------------------------
# Chiffres clés
# ---------------------------------------------------------------------------

STATS = [
    {
        "id": "stat-exp",
        "icon": "📅",
        "target": 15,
        "suffix": "+",
        "label": "Années d'Expérience",
        "description": "Au service du secteur pétrolier camerounais",
    },
    {
        "id": "stat-vol",
        "icon": "🛢️",
        "target": 500,
        "suffix": "M+",
        "label": "Litres Distribués / An",
        "description": "Volume annuel de produits pétroliers distribués",
    },
    {
        "id": "stat-part",
        "icon": "🤝",
        "target": 50,
        "suffix": "+",
        "label": "Partenaires Actifs",
        "description": "Fournisseurs et clients à travers le monde",
    },
    {
        "id": "stat-pays",
        "icon": "🌍",
        "target": 10,
        "suffix": "+",
        "label": "Pays Desservis",
        "description": "Présence commerciale en Afrique et dans le monde",
    },
]

# ---------------------------------------------------------------------------
# Politique QHSE-E
# ---------------------------------------------------------------------------

QHSE_INTRO = {
    "heading": "SAHARA OIL TRADING S.A.",
    "text": (
        "Société camerounaise spécialisée dans la distribution, l'importation "
        "et l'exportation de produits pétroliers, consciente des enjeux "
        "stratégiques, environnementaux et humains inhérents à ses activités, "
        "la Direction Générale s'engage à conduire l'ensemble de ses "
        "opérations en stricte conformité avec les principes suivants, "
        "applicables à tous les employés, sous-traitants, fournisseurs et "
        "partenaires de la société."
    ),
    "badges": [
        "🏅 Politique approuvée par la Direction Générale",
        "📋 Affichée sur les locaux & annexée aux appels d'offres",
        "🔄 Révisée périodiquement",
    ],
}

QHSE_PILLARS = [
    {
        "id": "qhse-quality",
        "icon": "🏆",
        "title": "Qualité",
        "featured": False,
        "description": (
            "Garantir à nos clients des produits pétroliers conformes aux "
            "normes nationales et internationales applicables, avec un service "
            "fiable et une traçabilité rigoureuse à chaque étape de la chaîne "
            "d'approvisionnement, de la collecte jusqu'à la livraison finale."
        ),
        "tags": ["ISO Standards", "Traçabilité Totale"],
    },
    {
        "id": "qhse-health",
        "icon": "🛡️",
        "title": "Santé & Sécurité",
        "featured": False,
        "description": (
            "Protéger la santé et la sécurité de nos employés, sous-traitants "
            "et communautés riveraines par l'application stricte des "
            "procédures HSE, la formation continue du personnel et le contrôle "
            "efficace des risques liés au stockage, au transport et à la "
            "manutention des produits pétroliers."
        ),
        "tags": ["Procédures HSE", "Formation Continue"],
    },
    {
        "id": "qhse-env",
        "icon": "🌿",
        "title": "Environnement",
        "featured": False,
        "description": (
            "Minimiser l'impact environnemental de nos activités en prévenant "
            "la pollution, en gérant les déchets et rejets de manière "
            "responsable, et en respectant les réglementations "
            "environnementales applicables au secteur pétrolier au Cameroun et "
            "dans la sous-région."
        ),
        "tags": ["Prévention Pollution", "Gestion Déchets"],
    },
    {
        "id": "qhse-ethics",
        "icon": "⚖️",
        "title": "Éthique & Intégrité",
        "featured": True,
        "description": (
            "Conduire nos activités avec transparence, équité et intégrité. "
            "SAHARA OIL TRADING S.A. applique une politique de tolérance zéro "
            "envers la corruption, la fraude et toute forme de pratique "
            "commerciale déloyale, conformément à la législation camerounaise "
            "et aux standards internationaux."
        ),
        "tags": ["Tolérance Zéro Corruption", "Conformité Légale"],
    },
    {
        "id": "qhse-contracts",
        "icon": "📝",
        "title": "Engagements Contractuels",
        "featured": False,
        "description": (
            "Respecter scrupuleusement les délais, volumes et conditions "
            "convenus avec nos clients et partenaires, et maintenir une "
            "communication transparente tout au long de l'exécution de chaque "
            "contrat."
        ),
        "tags": ["Délais Garantis", "Communication Transparente"],
    },
    {
        "id": "qhse-social",
        "icon": "🤝",
        "title": "Responsabilité Sociale",
        "featured": False,
        "description": (
            "Contribuer au développement économique local, favoriser l'emploi "
            "et la formation des talents nationaux, et entretenir des "
            "relations respectueuses avec les communautés locales et les "
            "autorités."
        ),
        "tags": ["Emploi Local", "Développement National"],
    },
    {
        "id": "qhse-improve",
        "icon": "📈",
        "title": "Amélioration Continue",
        "featured": False,
        "description": (
            "Mesurer régulièrement la performance de ses activités au regard "
            "de ces engagements et mettre en œuvre les actions correctives "
            "nécessaires pour réaliser une amélioration continue."
        ),
        "tags": ["Audits Réguliers", "Actions Correctives"],
    },
]

QHSE_CTA = {
    "title": "Politique disponible sur demande",
    "text": (
        "Cette politique est communiquée à tout le personnel, affichée dans "
        "les locaux de l'entreprise, annexée aux dossiers d'appels d'offres et "
        "mise à disposition de nos clients et partenaires."
    ),
    "button": "Demander la Politique Complète",
}

# ---------------------------------------------------------------------------
# Pourquoi nous choisir
# ---------------------------------------------------------------------------

WHY_CARDS = [
    {
        "id": "why-expertise",
        "icon": "🎯",
        "title": "Expertise Sectorielle",
        "description": (
            "Plus de 15 ans d'expérience dans le secteur des hydrocarbures en "
            "Afrique Centrale. Une connaissance approfondie des marchés locaux "
            "et internationaux."
        ),
    },
    {
        "id": "why-qualite",
        "icon": "✨",
        "title": "Qualité Garantie",
        "description": (
            "Tous nos produits sont soumis à des contrôles qualité rigoureux "
            "avant livraison. Conformité aux normes internationales ISO et aux "
            "réglementations locales."
        ),
    },
    {
        "id": "why-logistique",
        "icon": "🚛",
        "title": "Logistique Optimisée",
        "description": (
            "Flotte de camions-citernes modernes, réseau de dépôts "
            "stratégiques et partenariats maritimes pour des livraisons "
            "ponctuelles et sécurisées."
        ),
    },
    {
        "id": "why-support",
        "icon": "📞",
        "title": "Support 24/7",
        "description": (
            "Une équipe dédiée disponible à toute heure pour répondre à vos "
            "urgences d'approvisionnement et gérer vos commandes en temps réel."
        ),
    },
    {
        "id": "why-prix",
        "icon": "💰",
        "title": "Prix Compétitifs",
        "description": (
            "Grâce à nos achats groupés et notre réseau international, nous "
            "offrons des prix compétitifs sans compromettre la qualité de nos "
            "produits."
        ),
    },
    {
        "id": "why-durable",
        "icon": "🌱",
        "title": "Responsabilité Environnementale",
        "description": (
            "Engagement fort pour des pratiques respectueuses de "
            "l'environnement, réduction des émissions et conformité aux normes "
            "écologiques internationales."
        ),
    },
]

# ---------------------------------------------------------------------------
# Contact
# ---------------------------------------------------------------------------

CONTACT_ITEMS = [
    {
        "id": "contact-address",
        "icon": "📍",
        "title": "Siège Social",
        "lines": [CONTACT["city"], CONTACT["region"]],
    },
    {
        "id": "contact-phone",
        "icon": "📞",
        "title": "Téléphone",
        "lines": [CONTACT["phone"], CONTACT["hours"]],
    },
    {
        "id": "contact-email",
        "icon": "📧",
        "title": "Email",
        "lines": [CONTACT["email"], CONTACT["email_secondary"]],
    },
    {
        "id": "contact-ports",
        "icon": "🚢",
        "title": "Port Principal",
        "lines": [CONTACT["port"], CONTACT["port_detail"]],
    },
]

MARKETS = [
    "🇨🇲 Cameroun",
    "🇬🇦 Gabon",
    "🇨🇬 Congo",
    "🇨🇫 RCA",
    "🇹🇩 Tchad",
    "🇬🇶 Guinée Éq.",
]

# Valeurs autorisées pour le champ "service" du formulaire.
# La clé est la valeur envoyée, la valeur est le libellé affiché.
SERVICE_CHOICES = {
    "distribution": "Distribution Locale",
    "importation": "Importation",
    "exportation": "Exportation",
    "devis": "Demande de Devis",
    "partenariat": "Partenariat",
    "autre": "Autre",
}

# ---------------------------------------------------------------------------
# Pied de page
# ---------------------------------------------------------------------------

FOOTER = {
    "description": (
        "Votre partenaire de confiance pour la distribution, l'importation et "
        "l'exportation de produits pétroliers en Afrique Centrale depuis plus "
        "de 15 ans."
    ),
    "columns": [
        {
            "title": "Navigation",
            "links": [
                {"href": "#accueil", "label": "Accueil"},
                {"href": "#apropos", "label": "À Propos"},
                {"href": "#services", "label": "Services"},
                {"href": "#produits", "label": "Produits"},
                {"href": "#chiffres", "label": "Chiffres Clés"},
                {"href": "#contact", "label": "Contact"},
            ],
        },
        {
            "title": "Services",
            "links": [
                {"href": "#services", "label": "Distribution Locale"},
                {"href": "#services", "label": "Importation"},
                {"href": "#services", "label": "Exportation"},
                {"href": "#produits", "label": "Pétrole Brut"},
                {"href": "#produits", "label": "Carburants"},
                {"href": "#produits", "label": "Lubrifiants"},
                {"href": "#qhse", "label": "Politique QHSE-E"},
            ],
        },
    ],
    "quick_contact": [
        {"icon": "📍", "text": CONTACT["city"]},
        {"icon": "📞", "text": CONTACT["phone"]},
        {"icon": "📧", "text": CONTACT["email"]},
        {"icon": "🕒", "text": "Lun–Ven: 08h00–18h00"},
    ],
    "legal": ["Mentions Légales", "Politique de Confidentialité", "CGV"],
}

SOCIAL_LINKS = [
    {
        "id": "social-linkedin",
        "label": "LinkedIn",
        "url": "#",
        "svg": (
            '<svg viewBox="0 0 24 24" fill="currentColor">'
            '<path d="M16 8a6 6 0 016 6v7h-4v-7a2 2 0 00-2-2 2 2 0 00-2 2v7h-4v-7a6 6 0 016-6zM2 9h4v12H2z"/>'
            '<circle cx="4" cy="4" r="2" fill="currentColor"/></svg>'
        ),
    },
    {
        "id": "social-twitter",
        "label": "Twitter/X",
        "url": "#",
        "svg": (
            '<svg viewBox="0 0 24 24" fill="currentColor">'
            '<path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>'
        ),
    },
    {
        "id": "social-facebook",
        "label": "Facebook",
        "url": "#",
        "svg": (
            '<svg viewBox="0 0 24 24" fill="currentColor">'
            '<path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg>'
        ),
    },
]
