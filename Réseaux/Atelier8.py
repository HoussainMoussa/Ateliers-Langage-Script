import socket
import time

#Teste un socket avec un délai d'attente.
#recv() attend pendant un certain temps avant de lever une erreur.
def mesurer_timeout(sock, timeout):

    sock.settimeout(timeout)
    debut = time.perf_counter()

    try:
        sock.recv(1)
    except socket.timeout:
        pass

    return time.perf_counter() - debut

#Teste un socket en mode non bloquant.
#recv() retourne immédiatement si aucune donnée n'est disponible.
def mesurer_non_bloquant(sock):

    # Passage du socket en mode non bloquant.
    sock.setblocking(False)
    debut = time.perf_counter()

    try:
        sock.recv(1)
    except BlockingIOError:
        pass

    return time.perf_counter() - debut


def main():

    sockPair = socket.socketpair()
    a = sockPair[0]
    b = sockPair[1]

    with a, b:
        duree_timeout = mesurer_timeout(a, 0.2)
        duree_non_bloquant = mesurer_non_bloquant(b)

    print(f"Temps avec timeout de 0.2 s : {duree_timeout:.3f} seconde(s)")
    print(f"Temps en mode non bloquant  : {duree_non_bloquant:.6f} seconde(s)")

if __name__ == "__main__":
    main()


# Voici le résultat de l'éxécution: 
#Temps avec timeout de 0.2 s : 0.202 seconde(s)
#Temps en mode non bloquant  : 0.000039 seconde(s)


#Réponse
# On ne peut pas tester aussi facilement le mode bloquant car recv()
# attend indéfiniment tant qu'aucune donnée n'arrive, ce qui bloque le programme.
# Pour le tester correctement, il faudrait un autre thread ou processus
# capable d'envoyer une donnée après un certain délai.
