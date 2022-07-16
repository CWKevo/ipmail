import ipmail.settings as s
import re

from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlmodel import Session

from ipmail.database.engine import DATABASE
from ipmail.functions.mailing import create_ipmail, get_mails_for_ip, get_mail_by_id


MAIN_BLUEPRINT = Blueprint('main', __name__)



@MAIN_BLUEPRINT.route('/', methods=['GET'])
def index():
    """
        The main page.
    """

    return render_template('base.html')



@MAIN_BLUEPRINT.route('/ipmails', methods=['GET'])
def list_ipmails():
    """
        IPMails list
    """

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("page", 20, type=int)

    try:
        sent = request.args.get("sent", False, type=bool)

    except Exception:
        flash("Invalid value for `sent`.")
        return redirect(url_for('main.index'))


    ipmails = get_mails_for_ip(ip=request.remote_addr, page=page, per_page=per_page, sent=sent)

    return render_template('mails.html', ipmails=ipmails, current_page=page, state='sent' if sent else 'received')



@MAIN_BLUEPRINT.route('/send', methods=['POST'])
def send_ipmail():
    """
        Sends an IPMail.
    """

    for_ip =  request.form.get('for_ip', "").strip()
    subject = request.form.get('subject', "").strip()
    content = request.form.get('content', "").strip()

    if re.match(s.IP_REGEX, for_ip) is None or len(subject) > 65536 or len(content) < 1 or len(content) > 65536:
        flash("You must specify a valid target IP and IPMail's content.")
        return redirect(url_for('.index'))


    create_ipmail(for_ip=for_ip, content=content, subject=subject if len(subject) > 1 else None, from_ip=request.remote_addr)

    flash("IPMail was sent successfully.")
    return redirect(url_for('.index'))



@MAIN_BLUEPRINT.route('/remove', methods=['POST'])
def remove_ipmail():
    """
        Removes IPMail from user's ipmailbox
    """

    ipmail_id = request.form.get("id", None)

    if ipmail_id is None:
        flash("You must specify the ID of IPMail to delete.")
        return redirect(url_for('.index'))


    with Session(DATABASE) as session:
        ipmail = get_mail_by_id(ipmail_id=ipmail_id, for_ip=request.remote_addr)
        ipmail.visible_for_recipient = False

        session.add(ipmail)
        session.commit()

    flash("IPMail was successfully removed from your inbox.")
    return redirect(url_for('.index'))
