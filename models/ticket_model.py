from sqlalchemy import Column, Integer, String, Boolean, DateTime
from instance.database import db  

class Ticket(db.Model):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True)
    eventName = Column(String(100), nullable=False)
    location = Column(String(100), nullable=True)
    time = Column(DateTime, nullable=False)
    isUsed = Column(Boolean, default=False)
    
    
    __table_args__ = (
    db.Index('ix_ticket_eventName', 'eventName'),
    db.Index('ix_ticket_time', 'time'),
    )

    def __repr__(self):
        return f"<Ticket id={self.id} eventName={self.eventName} used={self.isUsed}>"

    def serialize(self):
        return {
        "id": self.id,
        "name": self.name,
        "is_used": self.is_used,
        "created_at": self.created_at.isoformat()
    }
    
