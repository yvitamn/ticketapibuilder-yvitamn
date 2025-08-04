from pathlib import Path
import sys 
import os
from flask import Flask
from flask_migrate import Migrate
from routers.ticket_router import ticket_bp
from config.database import initialize_database
from shared.error_handlers import register_error_handlers
from config.local import LocalConfig
from dotenv import load_dotenv
import importlib



def create_app(config_module="config.local.LocalConfig"):
    load_dotenv()  # Load environment variables from .env file
    
    # # 1. Environment Setup
    # flask_env = os.getenv("FLASK_ENV", "development")
    # load_environment_config(flask_env)
    
    # #  2. Configuration Loading     
    # config_class = get_config_class(config_class_path)
    
    # 3. Flask App Initialization   
    app = Flask(__name__)
    app.config.from_object(config_module)
        
    # 4. Database Setup
    from instance.database import migrate, ma, db
    initialize_database(app, db, migrate, ma)
        
    # 5. Register Components
    with app.app_context():
        from models.ticket_model import Ticket
        app.register_blueprint(ticket_bp)
        register_error_handlers(app)
        
    @app.route("/hello")
    def hello():
        return format_response({"message": "API is working!"})

    @app.route("/error")
    def error():
        # This will trigger 500
        raise Exception("Oops!")
          

    return app
        
 