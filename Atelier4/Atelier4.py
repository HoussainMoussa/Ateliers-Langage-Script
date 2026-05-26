import socket

def afficher_infos(nom, sock):
    print(nom)
    print("  fileno     :", sock.fileno())
    print("  getsockname:", sock.getsockname())
    print("  getpeername:", sock.getpeername())
    print()

def main():
    sockPair = socket.socketpair()
    a = sockPair[0]
    b = sockPair[1]
    with a, b:
        afficher_infos("Socket A", a)
        afficher_infos("Socket B", b)

if __name__ == "__main__":
    main()


#!!!!!! Réponse !!!!!!

#Les adresses sont vides car socket.socketpair() crée une paire de socket AF_UNIX anonyme
#Anonyme signifie ici qu’ils n’ont ni IP, ni port, ni nom dans le système de fichiers : 
#Ils existent seulement en mémoire et communiquent directement entre eux via le noyau.
#Un socket Unix anonyme n'a pas besoin d'adresse pour communiquer
#À l’inverse, un socket TCP/IPv4 classique doit avoir une adresse IP et un port pour être identifié sur le réseau et pouvoir communiquer avec d’autres machines. 
#C’est pour cela que getsockname() et getpeername() ne renvoient rien dans ce cas.
  
  
#Voici le résultat d'éxécution
#Socket A
#  fileno     : 3
#  getsockname:
#  getpeername:

#Socket B
#  fileno     : 4
#  getsockname:
#  getpeername:
