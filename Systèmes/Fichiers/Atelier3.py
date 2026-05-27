from datetime import datetime
import sys

def horodatage():

    date_time = datetime.datetime.now().isoformat(timespec="seconds")
    return date_time


def ecrire_log(msg):

    date_heure = horodatage()
    ligne = f"{date_heure} {msg}\n"
    with open("app.log", "a", encoding="utf-8") as f:
        f.write(ligne)


def main():

    if len(sys.argv) != 2:
        print("Erreur d'entrée. Usage: python3 atelier_03.py <message>")
        sys.exit(1)

    msg = sys.argv[1]
    ecrire_log(msg)


if __name__ == "__main__":
    main()


#Exemples d'éxécution avec un exemple d'éxecution avec nombre incorrect d'arguments
  

#[hmoussa@localhost fichiers]$ python3 atelier3.py "demarrage du service"
#[hmoussa@localhost fichiers]$ ls
#app.log  atelier3.py
#[hmoussa@localhost fichiers]$ python3 atelier3.py "traitement OK"
#[hmoussa@localhost fichiers]$ python3 atelier3.py "fin"
#[hmoussa@localhost fichiers]$ python3 atelier3.py "fin" "AAAA"
#Erreur d'entrée. Usage: python3 atelier_03.py <message>

  
#[hmoussa@localhost fichiers]$ cat app.log
#2026-05-27T12:30:59 demarrage du service
#2026-05-27T12:31:18 traitement OK
#2026-05-27T12:31:25 fin
