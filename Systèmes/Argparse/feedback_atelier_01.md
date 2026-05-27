# Feedback — Atelier 1 (S03 Argparse, MOUSSA El Houssein)

## Respect de la consigne

- `argparse` avec 3 arguments positionnels (deux floats + un opérateur via `choices`) ✓
- division par zéro gérée (stderr + `sys.exit(1)` quand fait correctement) ✓
- format de sortie type `a OP b = res` ✓

**Excellent** : modularité exemplaire avec `parser_arguments()` + `calculer()` + `afficher()` + `main()`. Les exemples d'exécution en commentaire (incluant `echo $?`) montrent que tu as vérifié le code retour.

---
*Évalué sur le commit `3eff772` (fichier `Systèmes/Argparse/Atelier1.py`).*
