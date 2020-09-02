from app import create_app
from app.config import AppConfig
from app.config.ssl import AppConfigSSL


app_config = AppConfig()


def use_ssl():
    ssl = AppConfigSSL.get_ssl_path()
    return ssl["public_key"], ssl["private_key"]


if __name__ == '__main__':
    # nohup sudo python -u __main__.py &

    app = create_app()
    app.run(**app_config.flask["flask"])
    # app.run(ssl_context=use_ssl(), **app_config.flask["flask"])
