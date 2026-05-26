import socket
import argparse


def tester_tcp(ip, port, timeout):
    # Création d'un socket TCP (AF_INET = IPv4, SOCK_STREAM = TCP) avec Définition d'un timeout
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((ip, port))
        except ConnectionRefusedError:
            # Le port est accessible mais refuse la connexion
            print(f"TCP → connexion refusée sur {ip}:{port}")
        except socket.timeout:
            #timeout réseau
            print(f"TCP → timeout, aucune réponse de {ip}:{port}")


def tester_udp(ip, port, timeout):
    # Création d'un socket UDP (SOCK_DGRAM = UDP)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # Envoi d'un ping=UDP vers la cible
        envoyes = s.sendto(b"ping", (ip, port))
        print(
            f"UDP → datagramme envoyé ({envoyes} octet(s)), "
            "aucune confirmation possible"
        )


def main():
    # Gestion des arguments en ligne de commande
    parser = argparse.ArgumentParser(
        description="Test TCP ou UDP sur 127.0.0.1:1"
    )

    # Choix du protocole à tester
    parser.add_argument(
        "--protocole",
        choices=["tcp", "udp"],
        required=True,
        help="Protocole à utiliser : tcp ou udp"
    )

    args = parser.parse_args()
  
    ip = "127.0.0.1"
    port = 1
    timeout = 1

    # Exécution selon le protocole choisi
    if args.protocole == "tcp":
        tester_tcp(ip, port, timeout)
    else:
        tester_udp(ip, port, timeout)

# Point d'entrée du script
if __name__ == "__main__":
    main()
