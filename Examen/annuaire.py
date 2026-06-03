import argparse
import logging
import os
import sys
from dotenv import load_dotenv
from client import (cmd_rechercher,cmd_enregistrer,cmd_compter,cmd_lister,configurer_serveur,)
from serveur import lancer_serveur


load_dotenv()

HOTE = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", "8888"))


def configurer_logging(niveau_verbosite: int) -> None:

    if niveau_verbosite == 0:
        niveau = logging.WARNING
        format_log = "%(message)s"

    elif niveau_verbosite == 1:
        niveau = logging.INFO
        format_log = "%(message)s"

    elif niveau_verbosite == 2:
        niveau = logging.DEBUG
        format_log = "%(message)s"

    else:
        niveau = logging.DEBUG
        format_log = (
            "%(asctime)s "
            "[%(threadName)s] "
            "%(name)s:%(lineno)d "
            "%(levelname)s - %(message)s"
        )

    logging.basicConfig(
        level=niveau,
        format=format_log,
        stream=sys.stderr,
    )


def main() -> None:

    parser = argparse.ArgumentParser(description="Annuaire réseau de domaines")

    parser.add_argument("-v",action="count",default=0,help="Augmente la verbosité (-v, -vv, -vvv)")

    sous_commandes = parser.add_subparsers(dest="commande",help="Commandes disponibles")

    parser_serveur = sous_commandes.add_parser("server",help="Lancer le serveur")
    parser_serveur.add_argument("--host",default=HOTE,help=f"Hôte d'écoute (défaut : {HOTE})")
    parser_serveur.add_argument("--port",type=int,default=PORT,help=f"Port d'écoute (défaut : {PORT})")

    parser_recherche = sous_commandes.add_parser("search",help="Rechercher un domaine")
    parser_recherche.add_argument("hote",help="Nom d'hôte à rechercher")
    parser_recherche.add_argument("--host", default=HOTE)
    parser_recherche.add_argument("--port",type=int,default=PORT)

    parser_enregistrement = sous_commandes.add_parser("record",help="Enregistrer un domaine")
    parser_enregistrement.add_argument("hote",help="Nom d'hôte à enregistrer")
    parser_enregistrement.add_argument("--host",default=HOTE)
    parser_enregistrement.add_argument("--port",type=int,default=PORT)


    parser_compter = sous_commandes.add_parser("count",help="Compter les domaines enregistrés")
    parser_compter.add_argument("--host",default=HOTE)
    parser_compter.add_argument("--port",type=int, default=PORT)

    parser_liste = sous_commandes.add_parser("list",help="Lister les domaines enregistrés")
    parser_liste.add_argument("--host",default=HOTE)
    parser_liste.add_argument("--port",type=int,default=PORT)

    args = parser.parse_args()
    configurer_logging(args.v)
    if not args.commande:
        parser.print_help()
        sys.exit(1)

    if args.commande == "server":
        lancer_serveur(args.host,args.port)

    elif args.commande == "search":
        configurer_serveur(args.host,args.port)
        domaine = cmd_rechercher(args.hote)
        if domaine is None:
            print(f"Domaine introuvable : {args.hote}",file=sys.stderr)
            sys.exit(1)

        print("=== Domaine trouvé ===")
        print("Hôte      :", domaine.hote)
        print("IP        :", domaine.ip)
        print("Contact   :", domaine.contact)
        print("Email     :", domaine.email)

    elif args.commande == "record":
        configurer_serveur(args.host,args.port)
        resultat = cmd_enregistrer(args.hote)
        print("Résultat :", resultat)
        if resultat != "OK":
            sys.exit(1)

    elif args.commande == "count":
        configurer_serveur(args.host,args.port)
        nombre = cmd_compter()
        print(f"Nombre de domaines enregistrés : {nombre}")

    elif args.commande == "list":
        configurer_serveur(args.host,args.port)
        domaines = cmd_lister()
        print("=== Domaines enregistrés ===")
        for hote in domaines:
            print("-", hote)


if __name__ == "__main__":
    main()
