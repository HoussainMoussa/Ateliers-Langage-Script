# Feedback — Atelier 1 (El Houssein MOUSSA)

## Respect de la consigne

Le contrat est rempli :

- validation `len(sys.argv) != 2` + `sys.exit(1)`,
- exception `socket.gaierror` rattrapée,
- IPv4 et IPv6 séparées et dédupliquées (`if ip not in ipv4`),
- total cohérent : `len(ipv4) + len(ipv6)`.

**Petit écart sur le format de sortie** : tu joins les adresses
avec `", "` sur une seule ligne :

```
IPv4 : 142.250.179.110
IPv6 : 2a00:1450:4007:80f::200e
```

Ça fonctionne quand il n'y a qu'une adresse par famille. Mais avec
plusieurs adresses (ex : `google.com` peut renvoyer 4-6 IPv4) ta
sortie sera :

```
IPv4 : 142.250.179.110, 142.250.179.142, 142.250.179.78
```

Alors que la consigne attend **une ligne par adresse** :

```
IPv4 : 142.250.179.110
IPv4 : 142.250.179.142
IPv4 : 142.250.179.78
```

Il suffit d'une boucle :
```python
for ip in ipv4: print(f"IPv4 : {ip}")
```

## Côté réseau

- Bon réflexe : déduplication explicite. Tu as compris que
  `getaddrinfo` peut produire plusieurs tuples par adresse.
- Le commentaire (lignes 10-11) qui rappelle un exemple de sortie
  de `getaddrinfo` est pédagogiquement utile pour toi : c'est une
  bonne habitude pour ancrer ce que retourne l'API.
- Indexation par position (`r[0]`, `r[4][0]`). Le dépaquetage nommé
  est plus lisible :
  ```python
  for famille, _t, _p, _c, sockaddr in res:
      ip = sockaddr[0]
  ```

## Côté Python (à titre indicatif)

- Excellente séparation des responsabilités : `resoudre()` calcule,
  `afficher()` imprime, `main()` orchestre. C'est le découpage que
  les copies les plus mûres adoptent. Bien.
- Garde `if __name__ == "__main__":` présente.
- Gestion d'erreur ciblée (`socket.gaierror`) et non un
  `except Exception` trop large. Bonne pratique.
- L'expression `", ".join(ipv4) if ipv4 else "aucune"` est
  intéressante : tu gères le cas vide explicitement. Pour respecter
  le format attendu, on s'en passe (on peut simplement ne rien
  afficher si la liste est vide).

---
*Évalué sur le commit `44a5c54` (fichier `Atelier1/Atelier1.py`).*
