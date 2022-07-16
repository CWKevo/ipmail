import typing as t

import sqlmodel as sql
from datetime import datetime



class IPMail(sql.SQLModel, table=True):
    """
        An IPMail.
    """

    __tablename__ = 'ipmails'
    id: t.Optional[int] = sql.Field(default=None, primary_key=True)
    """ID of the IPMail row in database."""

    from_ip: t.Optional[str]
    """What IP sent this IPMail?"""
    for_ip: str
    """To what IP should this IPMail be sent to?"""

    created_at: datetime = datetime.now()
    """When was the IPMail sent/created at."""
    subject: t.Optional[str]
    """The subject of the IPMail"""
    content: t.Text
    """The content of the IPMail"""

    visible_for_recipient: bool = True
    """Whether the IPMail is visible for the recipient (could be removed from their inbox)."""
