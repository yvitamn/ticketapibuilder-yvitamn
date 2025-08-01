from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validates, ValidationError
from models.ticket_model import Ticket
from datetime import datetime

class TicketSchema(SQLAlchemySchema):
    class Meta:
        model = Ticket
        load_instance = True
        # ordered = True

    id = auto_field(dump_only=True)
    eventName = auto_field(required=True)
    location = auto_field(required=True)
    time = auto_field(required=True)
    isUsed = auto_field(required=False)

    @validates("time")
    def validate_time(self, value):
        try:
            datetime.fromisoformat(value)
        except ValueError:
            raise ValidationError("Time must be in valid ISO format (e.g. 2025-07-31T12:00:00)")
