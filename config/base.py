import os
from dotenv import load_dotenv

load_dotenv() 

class BaseConfig:
   
    # SECRET_KEY = os.getenv("SECRET_KEY")  # No default here!
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    
    # JWT
    # JWT_ALGORITHM = "HS256"
    
    # Flask
    DEBUG = False
    TESTING = False
