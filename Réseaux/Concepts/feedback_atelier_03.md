# Feedback — Atelier 3 (El Houssein MOUSSA)

## Respect de la consigne

Très propre :

- argparse `--protocole tcp|udp` requis ✓
- TCP : `with` + `settimeout(1)` + capture séparée de
  `ConnectionRefusedError` et `socket.timeout` → messages clairs ✓
- UDP : `with` + `sendto` + nombre d'octets + message conforme ✓
- Structure exemplaire : fonctions `tester_tcp` / `tester_udp` +
  `main` + garde.

Note technique : tu n'as pas de gestion d'exception côté UDP — ce
n'est pas grave (l'envoi est censé toujours réussir au niveau de
l'API), c'est même le point pédagogique. Pour la robustesse on
peut ajouter `except OSError`, mais ce n'est pas obligatoire.

Les commentaires sont bien dosés et expliquent ce qu'on attend
(timeout, port refusant la connexion). Très bon rendu.

## Côté Python (à titre indicatif)

- Structure modulaire : on aime.
- Le commentaire de la ligne 12 « Le port est accessible mais
  refuse la connexion » est un peu approximatif — le service
  n'écoute pas du tout, donc le **noyau TCP** envoie le RST. La
  formulation usuelle est : « TCP signale immédiatement
  l'absence de service ».

---
*Évalué sur le commit `ef1e67c` (fichier `Réseaux/Concepts/Atelier3.py`).*
