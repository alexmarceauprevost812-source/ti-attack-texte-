#!/usr/bin/env python3
"""
Ti-Attack-Texte - Outil éducatif de cybersécurité
Penser comme un attaquant pour mieux se défendre.
Compatible : Termux • Kali Linux • Windows
"""

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
║          Penser comme un attaquant pour mieux se défendre    ║
╚══════════════════════════════════════════════════════════════╝
"""
    print(banner)

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


def afficher_menu():
    print("\n" + "─" * 50)
    print("              MENU PRINCIPAL")
    print("─" * 50)
    print("  1. Application / Site Web")
    print("  2. Serveur / Machine")
    print("  3. Réseau")
    print("  4. Application (Desktop / Mobile)")
    print("  5. Environnement Cloud")
    print("  6. Analyser TOUT")
    print("  0. Quitter")
    print("─" * 50)


def demander_cible():
    print("\nNom de la cible / laboratoire (ex: <labo-web>, <serveur-test>)")
    cible = input("→ ").strip()
    if not cible:
        cible = "<cible>"
    return cible


def main():
    afficher_banner()

    while True:
        afficher_menu()
        choix = input("\nChoisis une option : ").strip()

        if choix == "0":
            print("\n[+] Au revoir ! Reste prudent.")
            break

        types = {
            "1": "web",
            "2": "serveur",
            "3": "reseau",
            "4": "application",
            "5": "cloud",
            "6": "all"
        }

        if choix not in types:
            print("\n[!] Choix invalide. Réessaie.")
            continue

        type_choisi = types[choix]
        cible = demander_cible()

        print("\n" + "=" * 60)
        print(f"  Analyse en cours pour : {cible}")
        print("=" * 60)

        if type_choisi == "all":
            for t in TYPES_CIBLES:
                analyser_surface(cible, t)
                print()
        else:
            analyser_surface(cible, type_choisi)

        input("\nAppuie sur Entrée pour revenir au menu...")


if __name__ == "__main__":
    main()