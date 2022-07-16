import ipmail.settings as s
from ipmail.private_settings import SECRET_KEY

from flask import Flask


WEB = Flask(__name__)
WEB.config['SECRET_KEY'] = SECRET_KEY
WEB.config['DEBUG'] = s.DEBUG


from ipmail.web.blueprints import ALL_BLUEPRINTS
for blueprint in ALL_BLUEPRINTS:
    WEB.register_blueprint(blueprint)



@WEB.context_processor
def add_additional_context():
    return {
        'APP_NAME': s.APP_NAME,
        'APP_VERSION': s.APP_VERSION
    }



if __name__ == '__main__':
    WEB.run(host=s.WEB_HOST, port=s.WEB_PORT, debug=s.DEBUG)
