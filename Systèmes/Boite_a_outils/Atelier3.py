import secrets
import tempfile
from pathlib import Path


def generer_token():
    return secrets.token_urlsafe(32)


def ecrire_env(dossier: Path, token: str):

    fichier = dossier / ".env"
    fichier.write_text(f"TOKEN={token}\n", encoding="utf-8")
    return fichier


def lire_token(fichier: Path):

    ligne = fichier.read_text(encoding="utf-8").strip()
    _, _, valeur = ligne.partition("=")
    return valeur


def verifier(token_original: str, token_lu: str):

    return secrets.compare_digest(token_original, token_lu)


def main():

    with tempfile.TemporaryDirectory() as tmp:

        dossier = Path(tmp)
        token_original = generer_token()
        fichier = ecrire_env(dossier, token_original)
        token_lu = lire_token(fichier)

        print(f"fichier .env : {fichier}")
        print(f"contenu      : TOKEN={token_original}")
        print(f"lu           : {token_lu}")
        print(f"identique    : {verifier(token_original, token_lu)}")


if __name__ == "__main__":
    main()



#Sortie de l'éxécution

#fichier .env : /tmp/tmpxjqqpclk/.env
#contenu      : TOKEN=gw_4Lp9D78tOfDg3-viFoj9NPfZWcwxYsqteIZUHnJY
#lu           : gw_4Lp9D78tOfDg3-viFoj9NPfZWcwxYsqteIZUHnJY
#identique    : True
