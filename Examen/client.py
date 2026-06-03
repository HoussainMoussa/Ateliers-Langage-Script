import logging
import socket

from collecte import Domaine

logger = logging.getLogger(__name__)

HOTE = "127.0.0.1"
PORT = 8888


def configurer_serveur(hote: str, port: int) -> None:
    global HOTE, PORT
    HOTE = hote
    PORT = port


def envoyer_commande(commande: str, argument: str | None = None) -> str | None:

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(15)

        try:
            sock.connect((HOTE, PORT))

            # Construire le message texte simple
            if argument is not None:
                message = f"{commande} {argument}\n"
            else:
                message = f"{commande}\n"

            sock.sendall(message.encode("utf-8"))

            reponse = b""

            while True:
                bloc = sock.recv(1024)

                if not bloc:
                    break

                reponse += bloc

                if b"\n" in reponse:
                    break

            return reponse.decode("utf-8").strip()

        except ConnectionRefusedError:
            logger.error("Connexion refusée")
            return None

        except socket.timeout:
            logger.error("Timeout serveur")
            return None

        finally:
            sock.close()

    except Exception as e:
        logger.error(f"Erreur client : {e}")
        return None


def cmd_rechercher(hote: str) -> Domaine | None:

    reponse = envoyer_commande("SEARCH", hote)

    if reponse is None:
        return None

    if reponse.startswith("ERROR"):
        return None

    try:
        parties = reponse.split(maxsplit=4)
        if parties[0] != "OK" or len(parties) < 5:
            return None
        
        return Domaine(
            hote=parties[1],
            ip=parties[2],
            contact=parties[3] if parties[3] != "None" else None,
            email=parties[4] if parties[4] != "None" else None
        )

    except Exception as e:
        logger.error(f"Erreur parsing : {e}")
        return None


def cmd_enregistrer(hote: str) -> str:

    reponse = envoyer_commande("RECORD", hote)

    if reponse is None:
        return "ERROR"

    if reponse.startswith("OK"):
        return "OK"
    elif "EXISTE_DEJA" in reponse:
        return "EXISTE_DEJA"
    else:
        return "ERROR"


def cmd_compter() -> int:

    reponse = envoyer_commande("COUNT")

    if reponse is None:
        return 0

    if reponse.startswith("OK"):
        try:
            parties = reponse.split()
            return int(parties[1])
        except Exception:
            return 0
    
    return 0


def cmd_lister() -> list[str]:

    reponse = envoyer_commande("LIST")

    if reponse is None:
        return []

    if reponse.startswith("OK"):
        parties = reponse.split(maxsplit=1)
        if len(parties) > 1:
            return parties[1].split()
        return []
    
    return []
