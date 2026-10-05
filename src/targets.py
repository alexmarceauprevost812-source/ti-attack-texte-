"""
Définition des types de cibles et de leurs surfaces d'attaque typiques.
Tout est purement éducatif et utilise des placeholders.
"""

TYPES_CIBLES = {
    "web": {
        "nom": "Application / Site Web",
        "surfaces": [
            {
                "nom": "Authentification",
                "description": "Formulaires de login, gestion des sessions, réinitialisation de mot de passe",
                "ce_que_l_attaquant_regarde": [
                    "Présence de MFA / 2FA",
                    "Complexité des mots de passe acceptés",
                    "Gestion des sessions (cookies, tokens)",
                    "Messages d'erreur trop verbeux",
                    "Rate limiting sur les tentatives de connexion"
                ],
                "protections": [
                    "Activer MFA obligatoirement",
                    "Implémenter un rate limiting strict",
                    "Utiliser des tokens sécurisés (HttpOnly, Secure, SameSite)",
                    "Messages d'erreur génériques",
                    "Hashage fort des mots de passe (bcrypt/argon2)"
                ]
            },
            {
                "nom": "Injections (SQLi, XSS, Command Injection)",
                "description": "Points où des données utilisateur sont interprétées par le système",
                "ce_que_l_attaquant_regarde": [
                    "Champs de formulaires non filtrés",
                    "Paramètres d'URL",
                    "En-têtes HTTP",
                    "Uploads de fichiers"
                ],
                "protections": [
                    "Validation et sanitization strictes des entrées",
                    "Requêtes paramétrées / ORM",
                    "Content Security Policy (CSP)",
                    "Échapper correctement les sorties HTML",
                    "Principe du moindre privilège sur la base de données"
                ]
            },
            {
                "nom": "Gestion des sessions et cookies",
                "description": "Comment les sessions sont créées, stockées et invalidées",
                "ce_que_l_attaquant_regarde": [
                    "Cookies sans flags Secure / HttpOnly",
                    "Session fixation",
                    "Durée de vie trop longue des sessions",
                    "Prédiction des IDs de session"
                ],
                "protections": [
                    "Flags Secure + HttpOnly + SameSite=Strict",
                    "Régénération de session après login",
                    "Timeout de session raisonnable",
                    "Invalidation côté serveur à la déconnexion"
                ]
            },
            {
                "nom": "Exposition d'informations",
                "description": "Fuites d'informations techniques",
                "ce_que_l_attaquant_regarde": [
                    "Pages d'erreur détaillées",
                    "Headers serveur (Server, X-Powered-By)",
                    "Fichiers de backup / .git exposés",
                    "Commentaires dans le code source"
                ],
                "protections": [
                    "Désactiver les pages d'erreur détaillées en production",
                    "Supprimer les headers inutiles",
                    "Bloquer l'accès aux fichiers sensibles (.git, .env, backups)",
                    "Nettoyer le code avant déploiement"
                ]
            }
        ]
    },
    "serveur": {
        "nom": "Serveur / Machine",
        "surfaces": [
            {
                "nom": "Services exposés",
                "description": "Ports et services accessibles depuis l'extérieur",
                "ce_que_l_attaquant_regarde": [
                    "Ports ouverts inutiles",
                    "Versions des services (SSH, HTTP, FTP...)",
                    "Configurations par défaut",
                    "Comptes avec mots de passe faibles"
                ],
                "protections": [
                    "Fermer tous les ports non nécessaires",
                    "Utiliser un firewall strict",
                    "Mettre à jour régulièrement",
                    "Désactiver les comptes par défaut",
                    "Authentification par clé pour SSH"
                ]
            },
            {
                "nom": "Gestion des utilisateurs et privilèges",
                "description": "Comptes et droits sur le système",
                "ce_que_l_attaquant_regarde": [
                    "Comptes avec sudo sans mot de passe",
                    "Utilisateurs inutilisés",
                    "Permissions trop larges sur les fichiers"
                ],
                "protections": [
                    "Principe du moindre privilège",
                    "Audit régulier des comptes",
                    "Séparation des rôles",
                    "Surveillance des actions privilégiées"
                ]
            }
        ]
    },
    "reseau": {
        "nom": "Réseau",
        "surfaces": [
            {
                "nom": "Segmentation et isolation",
                "description": "Comment le réseau est divisé",
                "ce_que_l_attaquant_regarde": [
                    "Réseau plat (tout le monde peut parler à tout le monde)",
                    "Absence de VLAN / micro-segmentation",
                    "Accès latéral facile"
                ],
                "protections": [
                    "Segmentation réseau (VLAN, zones)",
                    "Firewall entre zones",
                    "Zero Trust Network Access",
                    "Surveillance du trafic latéral"
                ]
            },
            {
                "nom": "Protocoles et chiffrement",
                "description": "Sécurité des communications",
                "ce_que_l_attaquant_regarde": [
                    "Protocoles non chiffrés (HTTP, Telnet, FTP)",
                    "Certificats expirés ou auto-signés",
                    "Versions TLS obsolètes"
                ],
                "protections": [
                    "Forcer HTTPS / TLS 1.2+",
                    "Désactiver les protocoles faibles",
                    "Certificats valides et renouvelés",
                    "HSTS"
                ]
            }
        ]
    },
    "application": {
        "nom": "Application (Desktop / Mobile)",
        "surfaces": [
            {
                "nom": "Stockage local des données",
                "description": "Comment les données sensibles sont stockées sur l'appareil",
                "ce_que_l_attaquant_regarde": [
                    "Mots de passe en clair",
                    "Tokens d'API stockés sans protection",
                    "Bases de données non chiffrées"
                ],
                "protections": [
                    "Chiffrement des données au repos",
                    "Utilisation du Keychain / Keystore",
                    "Ne jamais stocker de secrets en clair"
                ]
            }
        ]
    },
    "cloud": {
        "nom": "Environnement Cloud",
        "surfaces": [
            {
                "nom": "Configuration IAM et permissions",
                "description": "Gestion des identités et des accès",
                "ce_que_l_attaquant_regarde": [
                    "Politiques trop permissives (*:*)",
                    "Clés d'accès exposées",
                    "Comptes de service trop puissants"
                ],
                "protections": [
                    "Principe du moindre privilège",
                    "Rotation régulière des clés",
                    "MFA sur tous les comptes",
                    "Audit des permissions"
                ]
            },
            {
                "nom": "Exposition publique des ressources",
                "description": "Buckets, bases de données, instances accessibles publiquement",
                "ce_que_l_attaquant_regarde": [
                    "Buckets S3 / stockage publics",
                    "Bases de données accessibles depuis Internet",
                    "Snapshots et backups exposés"
                ],
                "protections": [
                    "Tout privé par défaut",
                    "Vérification régulière des permissions publiques",
                    "Chiffrement des données",
                    "Logging et alertes"
                ]
            }
        ]
    }
}