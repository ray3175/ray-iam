from app import create_app
from app.config import AppConfig


if __name__ == '__main__':
    # nohup sudo python -u __main__.py &

    app = create_app("development")
    flask = AppConfig()["environment-development"]["flask"]
    app.run(**flask)
