import sys
import socket

def resoudre(domaine):
    ipv4 = []
    ipv6 = []
    #Récupérer les infos associés au domaine
    res = socket.getaddrinfo(domaine, None)
    for r in res:
        #en se basant sur la doc voici un exemple de la sortie de la commande
        #[(<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_DGRAM: 2>, 17, '', ('93.184.216.34', 80))]
        #récupérer la famille d'@
        famille = r[0]
        #récupérer l'@ IP
        ip = r[4][0]
        #Si c'est ipv4 ou ipv6 et fait pas déjà partie des listes on l'ajoute à la liste correspondante en utilisant append
        if famille == socket.AF_INET and ip not in ipv4:
            ipv4.append(ip)
        elif famille == socket.AF_INET6 and ip not in ipv6:
            ipv6.append(ip)
    return ipv4, ipv6

def afficher(ipv4, ipv6):
    print("IPv4 :", ", ".join(ipv4) if ipv4 else "aucune")
    print("IPv6 :", ", ".join(ipv6) if ipv6 else "aucune")
    print(f"Total : {len(ipv4) + len(ipv6)} enregistrement(s)")

def main():
    #Vérifie que l’utilisateur a bien fourni un DNS en argument
    if len(sys.argv) != 2:
        print("Usage: python atelier_01.py <nom_de_domaine>")
        sys.exit(1)

    #Récupère DNS passé en ligne de commande
    domaine = sys.argv[1]

    try:
        ipv4, ipv6 = resoudre(domaine)
    #Gère les erreurs liées à la résolution DNS
    except socket.gaierror as e:
        print(f"Erreur DNS: {e}")
        sys.exit(1)

    afficher(ipv4, ipv6)

if __name__ == "__main__":
    main()
