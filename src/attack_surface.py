"""
Module principal d'analyse des surfaces d'attaque.
Mode purement éducatif.
"""

from src.targets import TYPES_CIBLES


def analyser_surface(cible: str, type_cible: str):
    """
    Affiche une analyse éducative des surfaces d'attaque
    pour un type de cible donné.
    """
    if type_cible not in TYPES_CIBLES:
        print(f"[!] Type de cible inconnu : {type_cible}")
        return

    data = TYPES_CIBLES[type_cible]

    print(f"Cible           : {cible}")
    print(f"Type            : {data['nom']}")
    print("-" * 60)

    for i, surface in enumerate(data["surfaces"], 1):
        print(f"\n{i}. {surface['nom']}")
        print(f"   Description : {surface['description']}")

        print("\n   Ce que l'attaquant regarde :")
        for item in surface["ce_que_l_attaquant_regarde"]:
            print(f"   • {item}")

        print("\n   Comment se protéger :")
        for item in surface["protections"]:
            print(f"   ✓ {item}")

    print("\n" + "-" * 60)