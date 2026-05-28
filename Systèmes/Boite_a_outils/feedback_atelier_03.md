# Feedback — S13 Atelier 3 (Token URL-safe, MOUSSA El Houssein)

## Respect de la consigne

Critères attendus : `secrets.token_urlsafe(32)`, écriture/relecture dans un `.env` temporaire, comparaison via `secrets.compare_digest`

Constat sur ton code :
- ✓ `secrets.token_urlsafe(32)` utilisé (encapsulé dans `generer_token()`).
- ✓ `tempfile.TemporaryDirectory()` + `Path(tmp) / ".env"`, écriture `TOKEN={token}\n` via `ecrire_env`.
- ✓ Relecture et extraction via `ligne.partition("=")` dans `lire_token`.
- ✓ Comparaison via `secrets.compare_digest` dans `verifier`.
- ✓ Bonne décomposition en petites fonctions, sortie commentée en bas du fichier — soigné.

Découpage fonctionnel propre, tout est conforme.

---
*Évalué sur le commit `6ba5b50` (fichier `Systèmes/Boite_a_outils/Atelier3.py`).*
