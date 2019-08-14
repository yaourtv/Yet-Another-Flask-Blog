import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from flaskproj import mail, app

def save_pic(form_picture):
    _, f_ext = os.path.splitext(form_picture.filename)
    fname = secrets.token_hex(8) + f_ext
    thumb = Image.open(form_picture)
    thumb.thumbnail((125,125))
    thumb.save(os.path.join(app.root_path, 'static/profile_pics', fname))
    return fname

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                    sender='noreply@comfy.com',
                    recipients=[user.email])
    msg.body = f'''Password reset link is here:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request please just ignore this message. Kth.
'''
    mail.send(msg)
