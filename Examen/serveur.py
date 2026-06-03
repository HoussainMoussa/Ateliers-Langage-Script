"""
Protocol A : Texte ligne simple (COMMANDE argument\n).
Format lisible et testable avec netcat, cohérent avec le cours.
Chaque ligne est une commande, terminée par '\n'. Simple et efficace pour le débogage.
"""

import logging
import socketserver
from typing import Any
from collecte import collecter
from donnees import chercher, enregistrer, lister

logger = logging.getLogger(__name__)


class GestionnaireAnnuaire(socketserver.StreamRequestHandler):

    def handle(self) -> None:

        try:

            while True:

                ligne = self.rfile.readline().decode("utf-8").strip()
                if not ligne:
                    break
                
                try:
                    parties = ligne.split(maxsplit=1)
                    commande = parties[0].upper()
                    argument = parties[1] if len(parties) > 1 else None
                    
                except Exception:
                    logger.warning("Format de ligne invalide reçu")
                    self.envoyer_reponse("ERROR FORMAT_INVALIDE")
                    continue
                
                logger.info(f"Commande reçue : {commande}")
                
                if commande == "SEARCH":
                    self.traiter_search(argument)
                elif commande == "RECORD":
                    self.traiter_record(argument)
                elif commande == "COUNT":
                    self.traiter_count()
                elif commande == "LIST":
                    self.traiter_list()

                else:
                    self.envoyer_reponse("ERROR COMMANDE_INCONNUE")

        except Exception as e:
            logger.exception(f"Erreur gestionnaire : {e}")

    def traiter_search(self, hote: str | None) -> None:

        if not hote:
            self.envoyer_reponse("ERROR ARGUMENT_MANQUANT")
            return

        domaine = chercher(hote)

        if domaine is None:
            self.envoyer_reponse("ERROR NOT_FOUND")
            return

        self.envoyer_reponse(f"OK {domaine.hote} {domaine.ip} {domaine.contact} {domaine.email}")

    def traiter_record(self, hote: str | None) -> None:

        if not hote:
            self.envoyer_reponse("ERROR ARGUMENT_MANQUANT")
            return

        try:

            if chercher(hote):
                self.envoyer_reponse("ERROR EXISTE_DEJA")
                return

            domaine = collecter(hote)
            enregistrer(domaine)

            self.envoyer_reponse("OK")

        except Exception as e:

            logger.exception(f"Erreur RECORD : {e}")

            self.envoyer_reponse(f"ERROR {str(e)}")

    def traiter_count(self) -> None:

        try:
            domaines = lister()
            self.envoyer_reponse(f"OK {len(domaines)}")

        except Exception as e:

            logger.exception(f"Erreur COUNT : {e}")

            self.envoyer_reponse(f"ERROR {str(e)}")

    def traiter_list(self) -> None:

        try:

            domaines = lister()
            hotes = " ".join([domaine.hote for domaine in domaines])

            self.envoyer_reponse(f"OK {hotes}")

        except Exception as e:

            logger.exception(f"Erreur LIST : {e}")

            self.envoyer_reponse(f"ERROR {str(e)}")

    def envoyer_reponse(self, reponse: str) -> None:

        message = reponse + "\n"
        self.wfile.write(message.encode("utf-8"))


class ServeurAnnuaire(
    socketserver.ThreadingMixIn,
    socketserver.TCPServer
):
    allow_reuse_address = True


def lancer_serveur(hote: str, port: int) -> None:

    with ServeurAnnuaire((hote, port), GestionnaireAnnuaire) as serveur:

        logger.info(f"Serveur démarré sur {hote}:{port}")

        try:
            serveur.serve_forever()

        except KeyboardInterrupt:
            logger.info("Arrêt demandé par l'utilisateur")

        finally:
            serveur.server_close()
            logger.info("Serveur arrêté")
