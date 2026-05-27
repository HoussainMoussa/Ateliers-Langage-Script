import socket

def recv_ligne(sock):
    morceaux = []
    while True:
        #La lecture se fait octet par octet jusqu'au caractère \n
        octet = sock.recv(1)
        #Si le socket est fermé ou si \n est rencontré on arrête la lecture.
        if octet == b"\n" or octet == b"":
            break
        #ajout progressif des octets
        morceaux.append(octet)
    #resultat final
    return b"".join(morceaux)

def main():
    #Création d'un paire de socket
    sockPair = socket.socketpair()
    a = sockPair[0]
    b = sockPair[1]
    #Envoi de deux lignes par le socket a et lecture par le b
    with a, b:
        a.sendall(b"bonjour\nle monde\n")
        ligne1 = recv_ligne(b)
        ligne2 = recv_ligne(b)
        print("Ligne 1 :", ligne1)
        print("Ligne 2 :", ligne2)

if __name__ == "__main__":
    main()

#!!!!!! Bonus !!!!!!
#Cette méthode est inefficace en pratique car elle lit les données un octet à la fois avec recv(1). haque appel à recv() provoque un appel système, 
#ce qui coûte du temps et réduit les performances lorsqu’il y a beaucoup de données à traiter. Pour optimiser sans changer le comportement de la fonction,
#on peut utiliser un tableau dynamique afin de lire plusieurs octets d’un coup, puis rechercher le caractère \n directement dans les données déjà stockées en mémoire.


# Voici le résultat de l'éxécution
#Ligne 1 : b'bonjour'
#Ligne 2 : b'le monde'
