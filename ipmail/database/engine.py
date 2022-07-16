import typing as t
import ipmail.settings as s

from pathlib import Path
from sqlmodel import create_engine, SQLModel

# Need to move all models to the current namespace, so that SQLModel can create metadata for them.
from ipmail.database.models import IPMail


DATABASE_PATH = Path(__file__).parent / 'mails.db'
DATABASE = create_engine(rf'sqlite:///{DATABASE_PATH.absolute()}', echo=s.DEBUG)


ALL_MODELS: t.List[t.Type[SQLModel]] = [IPMail]
"""A container for all database models, mainly used to supress "Unused import" warnings."""

SQLModel.metadata.create_all(DATABASE)
