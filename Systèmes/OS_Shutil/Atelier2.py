import sys
import shutil
import os
from pathlib import Path
from datetime import datetime
import argparse


def parser_arguments():
    parser = argparse.ArgumentParser(description="Backup horodaté d'un dossier")
    parser.add_argument("dossier_source", help="Chemin du dossier à sauvegarder")
    return parser.parse_args()


def construire_destination(source):

    horodatage = datetime.now().strftime("%Y%m%d_%H%M%S")
    return source.parent / f"backup_{horodatage}"


def compter_fichiers(dossier):

    compteur = 0

    for racine, dirs, fichiers in os.walk(dossier):
        compteur += len(fichiers)

    return compteur


def copier(source, destination):

    shutil.copytree(source, destination)


def afficher(destination):

    print(f"Backup créé : {destination}")
    print(f"Fichiers copiés : {compter_fichiers(destination)}")


def main():

    args = parser_arguments()
    source = Path(args.dossier_source)

    # Vérification que le chemin donné est bien un dossier
    if not source.is_dir():
        print(f"Erreur : {source} n'est pas un dossier valide")
        sys.exit(1)

    destination = construire_destination(source)

    # Vérification de l'existence de la destination
    if destination.exists():
        print(f"Erreur : {destination} existe déjà")
        sys.exit(1)

    copier(source, destination)
    afficher(destination)


if __name__ == "__main__":
    main()


#Exemple d'éxécution avec succès

#mkdir test_dossier
#echo "bonjour" > test_dossier/a.txt
#echo "hello" > test_dossier/b.txt

#cat test_dossier/a.txt test_dossier/b.txt
#bonjour
#hello

#python3 atelier2.py test_dossier
#Backup créé : backup_20260527_152148
#Fichiers copiés : 2

#cat backup_20260527_152148/a.txt backup_20260527_152148/b.txt
#bonjour
#hello



#Exemple sans arguments
#python3 atelier2.py
#usage: atelier2.py [-h] dossier_source
#atelier2.py: error: the following arguments are required: dossier_source
  

#Exemple nombre incorrect d'arguments
#python3 atelier2.py dossier1 dossier2
#usage: atelier2.py [-h] dossier_source
#atelier2.py: error: unrecognized arguments: dossier2
  

#Exemple de dossier inexistant
#python3 atelier2.py /tmp/test_inexistant
#Erreur : /tmp/test_inexistant n'est pas un dossier valide
