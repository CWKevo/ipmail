import typing as t

from sqlmodel import Session, select, col, and_

from ipmail.database.engine import DATABASE
from ipmail.database.models import IPMail



def get_mails_for_ip(ip: str, page: int=1, per_page: int=20, sent: bool=False) -> t.List[IPMail]:
    """
        Obtains IPMails for specific IP address.
    """

    if page < 1 or per_page > 50:
        return []

    with Session(DATABASE) as session:
        if sent:
            return session.exec(select(IPMail).where(IPMail.from_ip == ip).offset((page - 1) * per_page).limit(per_page).order_by(col(IPMail.created_at).desc())).all()

        else:
            return session.exec(select(IPMail).where(and_(IPMail.for_ip == ip, IPMail.visible_for_recipient == True)).offset((page - 1) * per_page).limit(per_page).order_by(col(IPMail.created_at).desc())).all()



def create_ipmail(for_ip: str, content: t.Text, subject: t.Optional[str]=None, from_ip: t.Optional[str]=None) -> IPMail:
    """
        Created a new IPMail.
    """

    with Session(DATABASE) as session:
        ip_mail = IPMail(for_ip=for_ip, content=content, subject=subject, from_ip=from_ip)

        session.add(ip_mail)
        session.commit()

        return ip_mail



def get_mail_by_id(ipmail_id: int, for_ip: t.Optional[str]=None) -> t.Optional[IPMail]:
    """
        Obtains IPMail by its ID in the database.

        Specify `for_ip` to yield IPMail from their inbox - if it isn't addressed to them, return nothing.
    """

    with Session(DATABASE) as session:
        if for_ip:
            return session.exec(select(IPMail).where(and_(IPMail.id == ipmail_id, IPMail.for_ip == for_ip))).first()

        return session.exec(select(IPMail).where(IPMail.id == ipmail_id)).first()
