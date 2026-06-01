# Feedback — S06 Atelier 2 (Backup horodaté, MOUSSA El Houssein)

## Respect de la consigne

Critères attendus : `shutil.copytree(src, dst)` vers `backup_<strftime YYYYMMDD_HHMMSS>/`
placé à côté du source.

Constat sur ton code :

- ✓ `shutil.copytree` (préserve les métadonnées)
- ✓ `strftime("%Y%m%d_%H%M%S")` conforme
- ✓ nommage `backup_<timestamp>`
- ✓ destination placée dans `source.parent` (à côté du source, comme demandé)
- ✓ validation `source.is_dir()` avec message d'erreur + `sys.exit(1)`
- ✓ validation `destination.exists()` (évite l'écrasement)
- ✓ bonus : `argparse`, comptage des fichiers copiés, exemples d'exécution
  en commentaires (très bonne traçabilité)
- ✓ découpage en fonctions (`parser_arguments`, `construire_destination`,
  `compter_fichiers`, `copier`, `afficher`, `main`) — code modulaire propre

Excellent rendu — l'un des plus complets sur cet atelier.

---
*Évalué sur le commit `5f7f974` (fichier `Systèmes/OS_Shutil/Atelier2.py`).*
