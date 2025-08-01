from flask import Flask

def initialize_database(app: Flask, db, migrate, ma):        
    """Initialize database and migration"""
    try:      
        db.init_app(app)
        migrate.init_app(app,db)
        ma.init_app(app)
                     
        with app.app_context():
            connection = db.engine.connect()
            connection.close()
            print(f"✅ Database connection verified: {app.config.get('SQLALCHEMY_DATABASE_URI')}")
    except Exception as e:
        app.logger.error(f"❌ Database initialization failed: {str(e)}")
        raise 