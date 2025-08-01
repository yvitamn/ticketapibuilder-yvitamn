from typing import Any, Optional
from sqlalchemy.orm import Session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseRepository:
    def __init__(self, model: Any, db_session: Optional[Session] = None):
        self.model = model
        self.db_session = db_session or db.session

    def get_all(self):
        return self.db_session.query(self.model).all()

    def get_by_id(self, id: int):
        return self.db_session.get(self.model, id)

    def add(self, obj):
        self.db_session.add(obj)
        self.db_session.commit()
        self.db_session.refresh(obj)
        return obj

    def update(self, obj, data: dict):
        for key, value in data.items():
            setattr(obj, key, value)
        self.db_session.commit()
        return obj

    def delete(self, obj):
        self.db_session.delete(obj)
        self.db_session.commit()