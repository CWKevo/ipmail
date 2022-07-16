import typing as t

from flask import Blueprint

from ipmail.web.blueprints.main import MAIN_BLUEPRINT


ALL_BLUEPRINTS: t.List[t.Type[Blueprint]] = [
    MAIN_BLUEPRINT
]
