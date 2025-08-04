from sqlalchemy import Column, Integer, String, Boolean, DateTime
from instance.database import db  
from shared.database.chrono import utc_now

class Ticket(db.Model):
    __tablename__ = "ticket"

    id = db.Column(Integer, primary_key=True)
    eventName = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=True)
    time = db.Column(db.DateTime, default=utc_now, nullable=False)
    isUsed = db.Column(db.Boolean, default=False)
    
    
    __table_args__ = (
    db.Index('ix_ticket_eventName', 'eventName'),
    db.Index('ix_ticket_time', 'time'),
    )

    def __repr__(self):
        return f"<Ticket id={self.id} eventName={self.eventName} used={self.isUsed}>"

    def serialize(self):
        return {
        "id": self.id,
        "eventName": self.eventName,
            "location": self.location,
            "time": self.time.isoformat(),
            "isUsed": self.isUsed
    }
    
