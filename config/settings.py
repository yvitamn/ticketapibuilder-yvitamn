from pathlib import Path
import sys 
import os
from flask import Flask
from flask_migrate import Migrate
from config.blueprints import register_blueprints
from config.database import initialize_database
from config.error_handlers import register_error_handlers
from config.local import LocalConfig
from dotenv import load_dotenv
import importlib


def create_app(config_class_path=None):
    # 1. Environment Setup
    flask_env = os.getenv("FLASK_ENV", "development")
    load_environment_config(flask_env)
    
    #  2. Configuration Loading     
    config_class = get_config_class(config_class_path)
    
    # 3. Flask App Initialization   
    app = Flask(__name__)
    app.config.from_object(config_class)
        
    # 4. Database Setup
    from instance.database import migrate, ma, db
    initialize_database(app, db, migrate, ma)
        
    # 5. Register Components
    with app.app_context():
        from models import ticket_model
        register_blueprints(app)
        register_error_handlers(app)
          

    return app
        
 