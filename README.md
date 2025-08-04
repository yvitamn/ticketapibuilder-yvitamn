# ticketapibuilder-yvitamn


# Ticket Builder API



---

### Tech Stack

- Python 3.11+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate (Alembic)
- Supabase PostgreSQL (via shared pooling)
- Marshmallow (for validation)
- Dotenv for environment config
- uv

### Database Schema Overview

#### Entity Relationships


#### Models Included

- `Ticket`: 

### Setup Instructions

#### 1. Clone the Repository

```bash
git clone
cd ticketbuilderapi-yvitamn

```

#### 2. Create and Activate Virtual Env
- Make sure uv already installed and now activate venv
```bash 
uv venv
source .venv/bin/activate
```

#### 3. Install Dependencies
#####
```bash
uv add 
```

#### 4. Set Up Env Variables
FLASK_ENV=development
FLASK_APP=config.settings:create_app
DATABASE_URL=postgresql://YOUR_USER:YOUR_PASSWORD@YOUR_PROJECT.supabase.co:5432/postgres


### Database Migrations
 - We use Flask-Migrate (Alembic) for handling database migrations. For convenience, scripts are defined in the pyproject.toml

#### Go inside the env first, then run the aliases from the pyproject.toml


#### Initialize Alembic
- First time only

```bash
flask db init
```
#### Create Migration Script
- Generate migration from model changes

```bash
flask db migrate -m "Initial schema"
```
#### Apply Migration
- Apply to DB

```bash
flask db upgrade
```
#### Running the App

```bash
flask run
```


### Database Operations

#### CRUD Ticket



### Supabase Connection Notes

- This app uses Supabase shared connection pooling for PostgreSQL.

- The DATABASE_URL is defined in .env and automatically used via Flask-SQLAlchemy.

- Supabase setup is already integrated with SQLAlchemy and Alembic migrations.


