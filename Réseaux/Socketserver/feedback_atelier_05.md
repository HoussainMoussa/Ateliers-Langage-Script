# Feedback — Atelier 5 (R03 Socketserver, El Houssein MOUSSA)

> **Ré-évaluation à jour** après modification du source.

## Respect de la consigne

**Le fichier était vide précédemment — il est désormais complet**. Tout est
correct :

- `class ServeurMultiClient(socketserver.ThreadingMixIn, socketserver.TCPServer)`
  avec mixin en premier ✓
- `allow_reuse_address = True` ✓
- `BonjourHandler(StreamRequestHandler)` avec `time.sleep(2)` ✓
- `with ServeurMultiClient(...)` dans le `__main__` (pas le bug DAUPHIN/MOINE) ✓
- log par client ✓

Conforme au corrigé.

---
*Évalué sur le commit `a40125e` (fichier `Réseaux/Socketserver/Atelier5.py`).*

---

## Évaluation précédente (obsolète, commit `9d91b63`)

# Feedback — Atelier 5 (R03 Socketserver, El Houssein MOUSSA)

## Respect de la consigne

**Fichier vide** : `Réseaux/Socketserver/Atelier5.py` ne contient
aucun code. L'atelier n'a pas été rendu, ou un commit est passé
avec un fichier vide par accident.

À reprendre : voir le corrigé pour la trame attendue :

```python
import socketserver, time

class ServeurMultiClient(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True

class BonjourHandler(socketserver.StreamRequestHandler):
    def handle(self):
        ligne = self.rfile.readline().rstrip(b"\n")
        if not ligne: return
        time.sleep(2)
        self.wfile.write(b"Bonjour " + ligne + b".\n")

if __name__ == "__main__":
    with ServeurMultiClient(("127.0.0.1", 8808), BonjourHandler) as serveur:
        serveur.serve_forever()
```

Point clé : le `ThreadingMixIn` doit venir en premier (avant
`TCPServer`) dans l'héritage de la classe serveur.

---
*Évalué sur le commit `9d91b63` (fichier `Réseaux/Socketserver/Atelier5.py`).*

