# Feedback — Atelier 5 (S03 Argparse, MOUSSA El Houssein)

## Respect de la consigne

- argument positionnel `valeur` (type `float`) ✓
- drapeaux `--from` / `--to` avec `dest="depuis"`/`"vers"` (pour
  éviter les mots-clés Python) ✓
- `choices=["celsius", "fahrenheit", "kelvin"]` ✓
- `--precision` avec valeur par défaut 2 ✓
- format de sortie `<valeur> <unité> = <valeur> <unité>` avec
  précision dynamique ✓

Excellente modularité (parser_arguments + vers_celsius + depuis_celsius + convertir + afficher + main). **Détail** : tu vérifies manuellement `if args.depuis is None` au lieu d'utiliser `required=True` sur les `add_argument`. Le `required=True` est plus déclaratif (argparse génère le message d'erreur automatiquement).

---
*Évalué sur le commit `4f77901` (fichier `Systèmes/Argparse/Atelier5.py`).*
