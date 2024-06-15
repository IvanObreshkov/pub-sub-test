from dotenv import load_dotenv
from flask import Flask

from pub_sub_test.file_uploader import file_uploader_bp



def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(file_uploader_bp)

    return app


def start() -> None:
    create_app().run(host="0.0.0.0", port=3884)


if __name__ == '__main__':
    start()
