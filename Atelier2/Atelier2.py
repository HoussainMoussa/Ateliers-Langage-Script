import socket


def creer_sockets():

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    unix = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    return [
        ("TCP", tcp),
        ("UDP", udp),
        ("UNIX", unix),
    ]


def afficher_informations(sockets):
    for name, s in sockets:
        print(name)
        print("  fileno :", s.fileno())   # identifiant système du socket
        print("  family :", s.family.name)  # type d’adressage (AF_INET, AF_UNIX)
        print("  type   :", s.type.name)    # type de communication (TCP/UDP)
        print()


def main():
    # Création des sockets
    sockets = creer_sockets()
    afficher_informations(sockets)

if __name__ == "__main__":
    main()

# Réponse : Oui, les trois fileno() sont nécessairement différents.
# Chaque socket est une ressource ouverte dans la table des fichiers du système d'exploitation. Chaque appel à socket() crée une nouvelle entrée et se voit attribuer le plus petit entier disponible (ex: 3, 4, 5).
# Tant que les sockets restent ouverts (dans le with), leurs fd sont distincts.

#Voici la sortie de l'éxecution

#TCP
#  fileno : 3
#  family : AF_INET
#  type   : SOCK_STREAM

#UDP
#  fileno : 4
#  family : AF_INET
#  type   : SOCK_DGRAM

#UNIX
#  fileno : 5
#  family : AF_UNIX
#  type   : SOCK_STREAM
