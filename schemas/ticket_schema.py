from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validates, ValidationError
from models.ticket_model import Ticket
from datetime import datetime, timezone
from marshmallow.fields import DateTime

class TicketSchema(SQLAlchemySchema):
    class Meta:
        model = Ticket
        load_instance = True
        # ordered = True

    id = auto_field(dump_only=True)
    eventName = auto_field(required=True)
    location = auto_field(required=True)
    # Accept ISO datetime string from client, convert to datetime object
    time = auto_field(format="iso", required=True)
    isUsed = auto_field(required=False)

    @validates("time")
    def validate_time(self, value):
        if not isinstance(value, datetime):
            raise ValidationError("Time must be a valid datetime.")
        # Optional: enforce that time must be in the future
        if value < datetime.now(timezone.utc):
            raise ValidationError("Event time must be in the future.")