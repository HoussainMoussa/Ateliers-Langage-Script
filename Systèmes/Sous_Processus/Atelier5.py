import sys
import subprocess


def verifier_usage():

    #Vérif de l'argument
    if len(sys.argv) != 2:
        print("Usage: python3 atelier_05.py <programme>", file=sys.stderr)
        sys.exit(2)


def localiser(nom):

    return subprocess.run(
        ["which", nom],
        capture_output=True,
        text=True
    )


def main():

    verifier_usage()
    nom = sys.argv[1]
    try:
        result = localiser(nom)

    except FileNotFoundError:
        print("Erreur : 'which' introuvable sur le système", file=sys.stderr)
        sys.exit(1)

    # Si trouvé
    if result.returncode == 0:
        print(f"{nom} : {result.stdout.strip()}")
        sys.exit(0)

    # Sinon introuvable
    else:
        print(f"{nom} : introuvable")
        sys.exit(1)


if __name__ == "__main__":
    main()




#Exemple de l'éxécution

#python3 atelier5.py python3
#python3 : /usr/bin/python3
#python3 atelier5.py ls
#ls : /usr/bin/ls
#python3 atelier5.py toto
#toto : introuvable
#echo $?
#1
