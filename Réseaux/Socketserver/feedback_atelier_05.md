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
