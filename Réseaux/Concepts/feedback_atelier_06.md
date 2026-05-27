# Feedback — Atelier 6 (El Houssein MOUSSA)

## Respect de la consigne

Excellent rendu :

- `recv_exactement` correct ✓
- `envoyer_message` : préfixe 4 octets big-endian + `sendall` ✓
- `recevoir_message` : lit 4 octets, décode, lit la quantité ✓
- test avec `socketpair` dans un `with`, 3 messages,
  **comparaison explicite** avec impression « Message correct /
  incorrect » ✓
- bonus : sortie d'exécution incluse en commentaire en fin de
  fichier — facilite l'évaluation.

## Côté Python (à titre indicatif)

- Structure propre : 4 fonctions + `main` + garde.
- `sockPair = socket.socketpair() ; a = sockPair[0] ; b = sockPair[1]`
  — le dépaquetage est plus idiomatique :
  ```python
  a, b = socket.socketpair()
  ```
- Commentaires explicatifs au bon niveau de détail.

---
*Évalué sur le commit `3b6f79f` (fichier `Réseaux/Concepts/Atelier6.py`).*
