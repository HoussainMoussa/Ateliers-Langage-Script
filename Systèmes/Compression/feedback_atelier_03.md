# Feedback — S07 Atelier 3 (Extraire un .tar.gz en sécurité, MOUSSA El Houssein)

## Respect de la consigne

Critères attendus : créer une archive `.tar.gz` factice (dans un `tempfile`),
extraire avec `tar.extractall(cible, filter="data")`, lister le résultat.

Constat sur ton code :

- ✓ création d'une archive factice avec 3 fichiers (`notes.txt`, `rapport.txt`,
  `log.txt`)
- ✓ `tarfile.open(archive, "w:gz")` puis `tar.add(..., arcname=...)`
- ✓ `tar.extractall(cible, filter="data")` — extraction sécurisée
- ✓ listage via `cible.rglob("*")` après extraction
- ✓ bon découpage en fonctions (`creer_fichiers`, `creer_archive`,
  `extraire_archive`, `lister_fichiers`, `main`)
- ⚠ tu écris `archive.tar.gz`, `source_tmp/`, `cible/` dans le **CWD** au lieu
  de passer par `tempfile.TemporaryDirectory()`. Conséquence : les fichiers
  restent après exécution et polluent le dossier. Le corrigé utilise un
  tempdir pour tout nettoyer.
- ⚠ pas de gestion d'erreur (que se passe-t-il si `cible/` existe déjà ?)

Rendu fonctionnel, critère sécurité bien rempli (`filter="data"`).
Manque la propreté du tempfile.

---
*Évalué sur le commit `7f843e6` (fichier `Systèmes/Compression/Atelier3.py`).*
