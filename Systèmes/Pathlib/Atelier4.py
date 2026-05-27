from pathlib import Path


def decomposer (chemin: str) -> tuple[str, str, str]:

    p = Path(chemin)
    nom = p.stem
    extension = p.suffix
    dossier = str(p.parent)
    return (dossier, nom, extension)

def afficher(chemin):

    dossier, nom, extension = decomposer (chemin)
    print(f"{chemin:<30} -> ('{dossier}', '{nom}', '{extension}')")

def main():

    exemples = [
        "/tmp/a.txt",
        "/var/log/archive.tar.gz",
        "/etc/hosts",
        "/usr/local/bin/python3",
        "/var/www/html/index.html",
        "/home/ada/images/photo.jpeg",
        "/etc/nginx/nginx.conf",
    ]

    for chemin in exemples:
        afficher(chemin)

if __name__ == "__main__":
    main()



#Résultats de l'éxécution

#/tmp/a.txt                  -> ('/tmp', 'a', '.txt')
#/var/log/archive.tar.gz     -> ('/var/log', 'archive.tar', '.gz')
#/etc/hosts                  -> ('/etc', 'hosts', '')
#/usr/local/bin/python3      -> ('/usr/local/bin', 'python3', '')
#/var/www/html/index.html    -> ('/var/www/html', 'index', '.html')
#/home/ada/images/photo.jpeg -> ('/home/ada/images', 'photo', '.jpeg')
#/etc/nginx/nginx.conf       -> ('/etc/nginx', 'nginx', '.conf')
