from __future__ import with_statement
import logging
from logging.config import fileConfig

# from dotenv import load_dotenv
from flask import current_app

from alembic import context

import sys
import os

# Add your project's root directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# load_dotenv(dotenv_path='.env') 

# from flask_migrate import MigrateContext
from config.settings import create_app
from instance.database import db
from models.ticket_model import Ticket

# Initialize Flask app and SQLAlchemy
app = create_app()
# with app.app_context():
#     db = app.extensions['sqlalchemy'].db  # Access the `db` instance from Flask-SQLAlchemy
#     context = MigrateContext()
#     context.configure(bind=db.engine)
    
with app.app_context():
# Set target_metadata to `db.Model.metadata`
    target_metadata = db.Model.metadata

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config


# config.set_main_option('sqlalchemy.url', os.getenv('DATABASE_URL'))
# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)
logger = logging.getLogger('alembic.env')


def get_engine():
    return db.engine
    # try:
    #     # this works with Flask-SQLAlchemy<3 and Alchemical
    #     return current_app.extensions['migrate'].db.engine
    # except (TypeError, AttributeError):
    #     # this works with Flask-SQLAlchemy>=3
    #     return current_app.extensions['migrate'].db.engine


def get_engine_url():
    return str(get_engine().url).replace('%', '%%')
    # try:
    #     return get_engine().url.render_as_string(hide_password=False).replace(
    #         '%', '%%')
    # except AttributeError:
    #     return str(get_engine().url).replace('%', '%%')


# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

# config.set_main_option('sqlalchemy.url', get_engine_url()) # open this command if migrations offline
# target_db = current_app.extensions['migrate'].db

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


# def get_metadata():
#     if hasattr(target_db, 'metadatas'):
#         return target_db.metadatas[None]
#     return target_db.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, 
        target_metadata=target_metadata, 
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    
    with app.app_context():
        connectable = get_engine()
    # this callback is used to prevent an auto-migration from being generated
    # when there are no changes to the schema
    # reference: http://alembic.zzzcomputing.com/en/latest/cookbook.html
        def process_revision_directives(context, revision, directives):
            if getattr(config.cmd_opts, 'autogenerate', False):
                script = directives[0]
                if script.upgrade_ops.is_empty():
                    directives[:] = []
                    logger.info('No changes in schema detected.')

    # conf_args = current_app.extensions['migrate'].configure_args
    # if conf_args.get("process_revision_directives") is None:
    #     conf_args["process_revision_directives"] = process_revision_directives
  

        with connectable.connect() as connection:
            context.configure(
                connection=connection,
                target_metadata=target_metadata,
                compare_type=True,  # Optional: detect column type changes
                compare_server_default=True, # Optional: detect server default changes
                process_revision_directives=process_revision_directives,
                # **conf_args
            )

            with context.begin_transaction():
                context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
