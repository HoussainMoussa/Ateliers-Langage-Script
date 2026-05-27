import tarfile
from pathlib import Path


def creer_fichiers(dossier: Path) -> list:

    fichiers = [
        ("notes.txt", "Contenu du fichier notes.\n"),
        ("rapport.txt", "Contenu du fichier rapport.\n"),
        ("log.txt", "Contenu du fichier log.\n"),
    ]

    noms = []

    for nom, contenu in fichiers:
        (dossier / nom).write_text(contenu, encoding="utf-8")
        noms.append(nom)

    return noms


def creer_archive(dossier: Path, archive: Path):

    with tarfile.open(archive, "w:gz") as tar:
        for nom in creer_fichiers(dossier):
            tar.add(dossier / nom, arcname=nom)


def extraire_archive(archive: Path, cible: Path):

    with tarfile.open(archive, "r") as tar:
        tar.extractall(cible, filter="data")


def lister_fichiers(archive: Path):

    with tarfile.open(archive, "r") as tar:
        for nom in tar.getnames():
            print(f"  {nom}")


def main():

    dossier = Path("source_tmp")
    dossier.mkdir(exist_ok=True)

    archive = Path("archive.tar.gz")
    cible = Path("cible")

    creer_archive(dossier, archive)
    print(f"Archive créée : {archive}")

    print("Fichiers dans l'archive :")
    lister_fichiers(archive)

    extraire_archive(archive, cible)
    print(f"Fichiers extraits dans {cible} :")

    for fichier in cible.rglob("*"):
        if fichier.is_file():
            print(f"  {fichier}")


if __name__ == "__main__":
    main()


#Exemple de l'éxécution
#python3 atelier3.py
#Archive créée : /tmp/tmp257m1759/archive.tar.gz
#Fichiers dans l'archive :
#  notes.txt
#  rapport.txt
#  log.txt
#Fichiers extraits dans cible :
#  cible/notes.txt
#  cible/rapport.txt
#  cible/log.txt

#ls
#archive.tar.gz  atelier3.py  cible  source_tmp

#[hmoussa@localhost compression]$ cat cible/notes.txt
#Contenu du fichier notes.
#[hmoussa@localhost compression]$ cat cible/rapport.txt
#Contenu du fichier rapport.
#[hmoussa@localhost compression]$ cat cible/log.txt
#Contenu du fichier log.
