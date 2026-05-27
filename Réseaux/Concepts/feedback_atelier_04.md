# Feedback — Atelier 4 (El Houssein MOUSSA)

## Respect de la consigne

Très propre :

- `socket.socketpair()` ✓
- `with a, b:` ✓
- `fileno()`, `getsockname()`, `getpeername()` imprimés via une
  fonction `afficher_infos` (bonne factorisation) ✓
- Réponse à la question complète et précise :
  - adresses vides → AF_UNIX anonyme, pas d'IP/port/chemin ✓
  - « anonyme » → existent en mémoire seulement, communication
    via le noyau ✓
  - différence avec TCP/IPv4 → IP+port pour identification réseau ✓
- Bonus : tu inclus la sortie d'exécution en commentaire — utile
  pour montrer le résultat sans relancer le script.

Bonne pratique de copier-coller la sortie : ça permet à
l'évaluateur de comparer même sans Linux à portée de main.

## Côté Python (à titre indicatif)

- Structure modulaire : `afficher_infos` / `main` + garde.
- `sockPair = socket.socketpair() ; a = sockPair[0] ; b = sockPair[1]` —
  fonctionne, mais plus idiomatique :
  ```python
  a, b = socket.socketpair()
  ```
  Dépaquetage de tuple en une ligne.

---
*Évalué sur le commit `505ee66` (fichier `Réseaux/Concepts/Atelier4.py`).*
