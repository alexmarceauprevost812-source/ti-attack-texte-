#!/usr/bin/env python3
"""
Ti-Attack-Texte - Outil éducatif de cybersécurité
Penser comme un attaquant pour mieux se défendre.
"""

import argparse
from src.attack_surface import analyser_surface
from src.targets import TYPES_CIBLES


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

    args = parser.parse_args()

    print("=" * 60)
    print("  Ti-Attack-Texte - Mode éducatif")
    print("  Penser comme un attaquant pour mieux se défendre")
    print("=" * 60)
    print()

    if args.type == "all":
        for type_cible in TYPES_CIBLES:
            analyser_surface(args.cible, type_cible)
            print()
    else:
        analyser_surface(args.cible, args.type)

    print("\n[!] Rappel : Utilise uniquement sur des systèmes que tu possèdes ou en laboratoire.")


if __name__ == "__main__":
    main()