from config import Config
from flask_boilerplate import create_app, worker

app = create_app(Config(
    bootstrap=True,
    db=True,
    httpauth=True,
    mail=True,
    scheduler=True,
    auth=True,
    admin=False,
    index=True,
    wechat=True,
))

if __name__ == '__main__':
    app.config.update(DEBUG=True)
    app.run()
