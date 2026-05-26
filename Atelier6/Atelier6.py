import socket
import struct

def recv_exactement(sock, n):

    morceaux = []
    restant = n
    while restant:
        bloc = sock.recv(restant)
        if not bloc:
            raise ConnectionError("Connexion fermée prématurément")
        morceaux.append(bloc)
        restant -= len(bloc)
    return b"".join(morceaux)


def envoyer_message(sock, message: bytes) -> None:

    # Encodage de la longueur du message sur 4 octets avec l'option !I pour le format network
    longueur = struct.pack("!I", len(message))
    # Envoi de la longueur suivie du message
    sock.sendall(longueur + message)


def recevoir_message(sock) -> bytes:

    # Lecture des 4 octets contenant la longueur.
    header = recv_exactement(sock, 4)
    # Décodage de la longueur du message.
    longueur = struct.unpack("!I", header)[0]
    # Lecture du message complet.
    return recv_exactement(sock, longueur)


def main():

    #Création d'un paire de socket
    sockPair = socket.socketpair()
    a = sockPair[0]
    b = sockPair[1]

    # Envoi et réception avec socketpair
    with a, b:

        # Messages à envoyer.
        messages = [b"a", b"bb", b"ccc"]

        # Envoi des messages.
        for msg in messages:
            envoyer_message(a, msg)

        # Réception et vérification des messages.
        for original in messages:
            recu = recevoir_message(b)

            if recu == original:
                print("Message correct")
                print("Attendu :", original)
                print("Reçu    :", recu)
            else:
                print("Message incorrect")
                print("Attendu :", original)
                print("Reçu    :", recu)


if __name__ == "__main__":
    main()


#Résultat de l'éxécution
#Message correct
#Attendu : b'a'
#Reçu    : b'a'
#Message correct
#Attendu : b'bb'
#Reçu    : b'bb'
#Message correct
#Attendu : b'ccc'
#Reçu    : b'ccc'
