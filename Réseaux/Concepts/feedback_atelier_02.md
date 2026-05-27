# Feedback — Atelier 2 (El Houssein MOUSSA)

> **Note du formateur (mise à jour 2026-05-27)** : la présence ou
> l'absence de `AF_UNIX` n'est **plus prise en compte** dans la
> notation. Plusieurs étudiants travaillent sous Windows où cette
> famille de sockets n'est pas (ou peu) supportée. Les remarques
> ci-dessous qui critiquaient l'absence ou le remplacement de
> `AF_UNIX` (par `AF_INET6` notamment) sont à considérer comme
> **caduques**.


## Respect de la consigne

Tu as les trois sockets demandés, les bonnes infos imprimées, et
une réponse précise et bien argumentée à la question (« le plus
petit entier disponible », « tant que les sockets restent ouverts
leurs fd sont distincts »). Sortie commentée en fin de fichier
pour montrer la séquence 3, 4, 5. Tout cela est très bon.

**Point central manquant** : **pas de `with`**. Tu crées les
trois sockets avec `socket.socket(...)` simple et tu les laisses
ouvertes sans `close()`. La consigne demande explicitement « les
trois sockets dans un même `with` imbriqué » — c'est le concept
clé du module 02 : la gestion automatique du cycle de vie.

Solution :

```python
def creer_et_inspecter():
    with (socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp,
          socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp,
          socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as ux):
        for nom, s in (("TCP", tcp), ("UDP", udp), ("UNIX", ux)):
            print(f"{nom}  fileno={s.fileno()} "
                  f"family={s.family.name} type={s.type.name}")
```

Avec ça, les trois sockets sont garantis d'être fermés à la
sortie du bloc, même en cas d'exception.

## Côté Python (à titre indicatif)

- Bonne séparation des responsabilités (`creer_sockets`,
  `afficher_informations`, `main`).
- Garde `if __name__ == "__main__":` présente.

---
*Évalué sur le commit `eab5f88` (fichier `Réseaux/Concepts/Atelier2.py`).*
