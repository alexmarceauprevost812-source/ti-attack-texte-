#!/usr/bin/env python3
"""
Ti-Attack-Texte - Outil éducatif de cybersécurité
Penser comme un attaquant pour mieux se défendre.
Compatible : Termux • Kali Linux • Windows
"""

import argparse
import platform
import sys
from src.attack_surface import analyser_surface
from src.targets import TYPES_CIBLES


def afficher_banner():
    banner = r"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ████████╗██╗       █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗
║   ╚══██╔══╝██║      ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝
║      ██║   ██║      ███████║   ██║      ██║   ███████║██║     █████╔╝ 
║      ██║   ██║      ██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗ 
║      ██║   ███████╗██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗
║      ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
║                                                              ║
║                    T E X T E                                 ║
║                                                              ║
║          Penser comme un attaquant pour mieux se défendre    ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
    print(banner)

    # Détection de l'environnement
    systeme = platform.system()
    if "android" in platform.platform().lower() or "termux" in sys.executable.lower():
        env = "Termux (Android)"
    elif systeme == "Linux":
        env = "Linux (Kali / Ubuntu / etc.)"
    elif systeme == "Windows":
        env = "Windows"
    else:
        env = systeme

    print(f"  Environnement détecté : {env}")
    print(f"  Mode                  : Éducatif uniquement")
    print("=" * 64)
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Ti-Attack-Texte - Analyse éducative des surfaces d'attaque"
    )
    parser.add_argument(
        "--type",
        choices=list(TYPES_CIBLES.keys()) + ["all"],
        default="all",
        help="Type de cible à analyser (web, serveur, reseau, application, cloud)"
    )
    parser.add_argument(
        "--cible",
        default="<cible>",
        help="Nom de la cible (placeholder recommandé, ex: <labo-web>)"
    )
    parser.add_argument(
        "--no-banner",
        action="store_true",
        help="Ne pas afficher le banner"
    )

    args = parser.parse_args()

    if not args.no_banner:
        afficher_banner()

    if args.type == "all":
        for type_cible in TYPES_CIBLES:
            analyser_surface(args.cible, type_cible)
            print()
    else:
        analyser_surface(args.cible, args.type)

    print("\n[!] Rappel : Utilise uniquement sur des systèmes que tu possèdes ou en laboratoire.")
    print("[!] Placeholders uniquement (<cible>, <labo>, etc.)")


if __name__ == "__main__":
    main()