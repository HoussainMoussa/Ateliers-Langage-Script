# Annuaire - Répertoire de domaines en réseau

Application Python pour gérer un répertoire de noms d'hôtes, adresses IP et informations WHOIS.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Lancer le serveur

```bash
python cli.py serve
```

### Enregistrer un domaine

```bash
python cli.py record google.com
```

### Chercher un domaine

```bash
python cli.py search google.com
```

### Lister les domaines

```bash
python cli.py list
```

### Compter les domaines

```bash
python cli.py count
```

## Protocol

Format simple: `COMMANDE argument\n`

Exemples:
```
SEARCH google.com
RECORD github.com
COUNT
LIST
```

Réponses:
```
OK google.com 159.31.10.2 Google email@example.com
OK
ERROR ALREADY_EXISTS
OK 2
OK google.com github.com
```

## Structure

- `cli.py` - Interface en ligne de commande
- `serveur.py` - Serveur TCP multi-threadé
- `client.py` - Client socket
- `collecte.py` - Collection de données (nslookup, whois)
- `donnees.py` - Base de données SQLite
- `test_donnees.py` - Tests unitaires

## Base de données

Table `domaines`:
- `hote` (String, clé primaire)
- `ip` (String)
- `contact` (String)
- `email` (String)

## Variables d'environnement

Dans `.env`:
```
HOST=127.0.0.1
PORT=8888
```

## Tests

```bash
pytest test_donnees.py -v
```

## Licence

MIT
