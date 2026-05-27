import socketserver
import time

socketserver.TCPServer.allow_reuse_address = True

HOTE = "127.0.0.1"
PORT = 8808


class ServeurMultiClient(socketserver.ThreadingMixIn, socketserver.TCPServer):
    # Les threads clients se ferment automatiquement à l'arrêt du serveur.
    daemon_threads = True


class BonjourHandler(socketserver.StreamRequestHandler):

    def handle(self) -> None:
        ligne = self.rfile.readline().rstrip(b"\n")
        if not ligne:
            return
        print(f"    Reçu de {self.client_address} : {ligne!r}")
        time.sleep(2)
        self.wfile.write(b"Bonjour " + ligne + b".\n")


def demarrer_serveur():

    with ServeurMultiClient((HOTE, PORT), BonjourHandler) as serveur:
        print(f"<<< ServeurMultiClient en attente sur {(HOTE, PORT)}")
        print("    (Ctrl-C pour arrêter)")
        serveur.serve_forever()


def main():

    demarrer_serveur()


if __name__ == "__main__":
    main()



#Exemple d'éxécution

#Terminal principal
#<<< ServeurMultiClient en attente sur ('127.0.0.1', 8808)
#    (Ctrl-C pour arrêter)
#    Reçu de ('127.0.0.1', 47482) : b'Alice'
#    Reçu de ('127.0.0.1', 44568) : b'Bob'

#Terminal 1
#echo "Alice" | ncat 127.0.0.1 8808
#Bonjour Alice.

#Terminal 2
#echo "Bob" | nc 127.0.0.1 8808
#Bonjour Bob.
