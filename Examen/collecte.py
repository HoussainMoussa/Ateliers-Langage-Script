import logging
import platform
import re
import subprocess

from pydantic import BaseModel, EmailStr

logger = logging.getLogger(__name__)


class Domaine(BaseModel):
    hote: str
    ip: str | None = None
    contact: str | None = None
    email: EmailStr | None = None


def resoudre_ip(hote: str) -> str | None:

    systeme = platform.system()

    try:

        if systeme == "Windows":

            resultat = subprocess.run(
                ["nslookup", hote],
                capture_output=True,
                text=True,
                timeout=5.0
            )

            if resultat.returncode != 0:
                return None

            sortie = resultat.stdout

        else:

            try:

                resultat = subprocess.run(
                    ["host", hote],
                    capture_output=True,
                    text=True,
                    timeout=5.0
                )

                if resultat.returncode == 0:

                    match = re.search(
                        r"has address (\d+\.\d+\.\d+\.\d+)",
                        resultat.stdout
                    )

                    if match:
                        return match.group(1)

            except FileNotFoundError:
                pass

            resultat = subprocess.run(
                ["nslookup", hote],
                capture_output=True,
                text=True,
                timeout=5.0
            )

            if resultat.returncode != 0:
                return None

            sortie = resultat.stdout

        match = re.search(
            r"Address:\s*(\d+\.\d+\.\d+\.\d+)",
            sortie
        )

        if match:
            return match.group(1)

        return None

    except (subprocess.TimeoutExpired, FileNotFoundError):
        return None


def interroger_whois(hote: str) -> tuple[str | None, str | None]:

    try:

        resultat = subprocess.run(
            ["whois", hote],
            capture_output=True,
            text=True,
            timeout=10.0
        )

        if resultat.returncode != 0:
            return (None, None)

        texte = resultat.stdout

        contact = None

        motifs_contact = [
            r"Registrant Name:\s*(.+)",
            r"Registrant:\s*(.+)"
        ]

        for motif in motifs_contact:

            match = re.search(
                motif,
                texte,
                re.IGNORECASE
            )

            if match:
                contact = match.group(1).strip()
                break

        match_email = re.search(
            r"\S+@\S+",
            texte,
            re.IGNORECASE
        )

        email = match_email.group(0) if match_email else None

        return (contact, email)

    except (subprocess.TimeoutExpired, FileNotFoundError):
        return (None, None)


def collecter(hote: str) -> Domaine:

    logger.info(f"Collecte des informations pour {hote}")

    ip = resoudre_ip(hote)

    contact, email = interroger_whois(hote)

    return Domaine(
        hote=hote,
        ip=ip,
        contact=contact,
        email=email
    )


if __name__ == "__main__":

    domaine = collecter("google.com")

    print(domaine.model_dump())
