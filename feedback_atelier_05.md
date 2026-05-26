# Feedback — Atelier 5 (El Houssein MOUSSA)

## Respect de la consigne

Excellent rendu :

- `recv_ligne(sock)` lit octet par octet, gère `b""` (EOF) et
  `b"\n"` dans la même condition ✓
- délimiteur non inclus ✓
- test avec `socketpair` dans un `with`, envoi correct, deux
  appels `recv_ligne` ✓
- réponse au bonus complète et précise : « lit un octet à la
  fois → un appel système par recv → coûteux ; pour optimiser,
  un tableau dynamique pour lire plusieurs octets d'un coup,
  puis rechercher `\n` en mémoire » ✓

C'est un rendu modèle, sur le fond et la forme.

## Côté Python (à titre indicatif)

- Structure : `recv_ligne` + `main` + garde — bonne pratique.
- `sockPair = socket.socketpair(); a = sockPair[0]; b = sockPair[1]`
  — fonctionne, mais le dépaquetage est plus idiomatique :
  ```python
  a, b = socket.socketpair()
  ```
- Commentaires explicatifs au bon niveau de détail.
- Bonus pédagogique : tu inclus la sortie d'exécution en fin de
  fichier, ce qui aide l'évaluation.

---
*Évalué sur le commit `b81aa78` (fichier `Atelier1/Atelier5.py`).*
