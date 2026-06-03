from pathlib import Path
from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import Session
from sqlalchemy.orm import mapped_column

from collecte import Domaine

BDD_PATH = Path(__file__).parent / "domaines.db"


class Base(DeclarativeBase):
    pass


class DomaineORM(Base):
    __tablename__ = "domaines"

    hote: Mapped[str] = mapped_column(String, primary_key=True)
    ip: Mapped[str | None] = mapped_column(String, nullable=True)
    contact: Mapped[str | None] = mapped_column(String, nullable=True)
    email: Mapped[str | None] = mapped_column(String, nullable=True)


engine = create_engine(f"sqlite:///{BDD_PATH}")

Base.metadata.create_all(engine)


def enregistrer(domaine: Domaine) -> None:

    with Session(engine) as session:

        existe = session.get(DomaineORM, domaine.hote)

        if existe is not None:
            raise ValueError("Domaine déjà enregistré")

        objet = DomaineORM(
            hote=domaine.hote,
            ip=domaine.ip,
            contact=domaine.contact,
            email=domaine.email,
        )

        session.add(objet)
        session.commit()


def lister() -> list[Domaine]:

    with Session(engine) as session:

        lignes = session.scalars(
            select(DomaineORM)
        ).all()

        return [
            Domaine(
                hote=ligne.hote,
                ip=ligne.ip,
                contact=ligne.contact,
                email=ligne.email,
            )
            for ligne in lignes
        ]


def chercher(hote: str) -> Domaine | None:

    with Session(engine) as session:

        ligne = session.get(DomaineORM, hote)

        if ligne is None:
            return None

        return Domaine(
            hote=ligne.hote,
            ip=ligne.ip,
            contact=ligne.contact,
            email=ligne.email,
        )
