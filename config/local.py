#default config
import os
from dotenv import load_dotenv
from config.base import BaseConfig

# Path configuration
config_dir = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.dirname(config_dir)
instance_dir = os.path.join(project_root, "instance")
os.makedirs(instance_dir, exist_ok=True)  # Create if missing

load_dotenv() 

class LocalConfig(BaseConfig):
    DEBUG = True
    
    DB_PASSWORD = "0goKcnBB94G6LTMo"  
    DB_USER = ""  
    DB_NAME = "postgres"  
    DB_HOST = "aws-0-us-east-2.pooler.supabase.com"
    DB_PORT = 5432  
    # postgresql://postgres.ipavhgmapltdbglfqbuz:[YOUR-PASSWORD]@aws-0-us-east-2.pooler.supabase.com:5432/postgres
    
    # SECRET_KEY = "super-secret-key"  # You can load this from env if needed
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", 
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    
    # Security configurations
    # SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")  # Never hardcode in prod
    
    # JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt_dev_key")
    
    # JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256") 
    
    # Disable CSRF protection in development
    WTF_CSRF_ENABLED = False
   
   # SQLALCHEMY_TRACK_MODIFICATIONS = False
    