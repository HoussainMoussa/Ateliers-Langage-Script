# Feedback — R00 Atelier 8 (Deux modes d'attente, MOUSSA El Houssein)

## Respect de la consigne

Critères attendus : comparer le temps d'attente entre `socket.timeout`
(mode bloquant avec timeout) et un autre mode (non bloquant ou `select`).

Constat sur ton code :

- ✓ deux fonctions séparées (`mesurer_timeout`, `mesurer_non_bloquant`)
- ✓ `socket.socketpair()` + `with` propre
- ✓ mesure via `time.perf_counter()`
- ✓ exception `socket.timeout` et `BlockingIOError` correctement attrapées
- ✓ résultats commentés montrent la différence (0.202s vs 0.000039s)
- ✓ réponse à la question bonus pertinente (pourquoi on ne peut pas
  facilement tester le mode bloquant : il faudrait un thread/processus)
- ⚠ le critère mentionnait `select.select()` comme alternative — toi tu
  utilises `setblocking(False)` + `BlockingIOError`. Les deux sont valables
  pédagogiquement (non bloquant et select sont conceptuellement proches),
  mais le corrigé fait `select` qui montre l'attente avec timeout côté OS.
- ⚠ `sockPair[0]` / `sockPair[1]` plus lisible avec un tuple unpacking :
  `a, b = socket.socketpair()`

Rendu solide, bien commenté, choix techniques défendables.

---
*Évalué sur le commit `de213a9` (fichier `Réseaux/Concepts/Atelier8.py`).*
