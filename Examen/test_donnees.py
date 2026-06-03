import pytest

from collecte import Domaine
from donnees import enregistrer
from donnees import chercher
from donnees import lister


def test_enregistrer_et_chercher():

    domaine = Domaine(
        hote="example.com",
        ip="1.1.1.1",
        contact="Test",
        email="test@example.com",
    )

    try:
        enregistrer(domaine)
    except ValueError:
        pass

    resultat = chercher("example.com")

    assert resultat is not None
    assert resultat.hote == "example.com"


def test_chercher_inexistant():

    resultat = chercher("inexistant-xyz.com")

    assert resultat is None


def test_lister():

    resultat = lister()

    assert isinstance(resultat, list)


def test_validation_email():

    domaine = Domaine(
        hote="test.com",
        ip="1.1.1.1",
        contact="Test",
        email="test@test.com",
    )

    assert domaine.email == "test@test.com"

    with pytest.raises(Exception):

        Domaine(
            hote="test.com",
            ip="1.1.1.1",
            contact="Test",
            email="email-invalide",
        )
