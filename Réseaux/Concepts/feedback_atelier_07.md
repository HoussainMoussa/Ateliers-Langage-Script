# Feedback — R00 Atelier 7 (Trois lectures bytes, MOUSSA El Houssein)

## Respect de la consigne

Critères attendus : trois lectures des mêmes 4 octets (big-endian, little-endian,
inversé + big-endian), démontrer l'équivalence entre les deux dernières.

Constat sur ton code :

- ✓ `struct.unpack("!I", ...)` pour big-endian
- ✓ `struct.unpack("<I", ...)` pour little-endian
- ✓ `struct.unpack("!I", brut[::-1])` pour inversé + big-endian
- ✓ vérification explicite `little_endian == inverse` imprimée
- ✓ réponse rédigée en commentaire : explication claire et juste
- ✓ résultat d'exécution conservé en commentaire (bonne traçabilité)
- ⚠ utilise uniquement `struct.unpack` ; le corrigé utilise `int.from_bytes`
  (plus pythonique pour des entiers simples). Pas grave, juste un autre idiome.

Rendu très propre et la réponse à la question bonus est bien construite.

---
*Évalué sur le commit `9c8e3d6` (fichier `Réseaux/Concepts/Atelier7.py`).*
