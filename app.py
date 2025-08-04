# def main():
#     print("Hello from ticketapibuilder-yvitamn!")

from instance.database import db
from config.settings import create_app


app = create_app("config.local.LocalConfig")  


# FlaskInjector(app=app, modules=[configure])
# Initialize Flask-Migrate with the app and db instance
#Explicitly expose app instance for Flask CLI

if __name__ == "__main__":
    app.run()
