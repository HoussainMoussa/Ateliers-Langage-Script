# Feedback — S08 Atelier 5 (Mini `which`, MOUSSA El Houssein)

## Respect de la consigne

Critères attendus : `subprocess.run(["which", nom])`, gérer code retour 0/!=0, gérer `FileNotFoundError` (which absent)

Constat sur ton code :
- ✓ `subprocess.run(["which", nom], capture_output=True, text=True)` conforme.
- ✓ Branche `returncode == 0` : chemin imprimé avec `.strip()`.
- ✓ Branche `returncode != 0` : `<nom> : introuvable` + `sys.exit(1)`.
- ✓ `FileNotFoundError` capturé avec message stderr et `sys.exit(1)`.
- ✓ Bonus usage : `len(sys.argv) != 2` géré, message stderr + `sys.exit(2)`.
- ⚠ Pas de `timeout` (bonus optionnel).
- ✓ Découpage en fonctions `verifier_usage` / `localiser` / `main`, code propre.

---
*Évalué sur le commit `f96c1b2` (fichier `Systèmes/Sous_Processus/Atelier5.py`).*
