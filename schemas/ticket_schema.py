from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import ValidationError, validates_schema
from models.ticket_model import Ticket
from datetime import datetime, timedelta, timezone
from marshmallow.fields import DateTime
from instance.database import db
from shared.database.chrono import utc_now


class TicketSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Ticket
        load_instance = True
        # ordered = True
        sqla_session = db.session

    # id = fields.Int(dump_only=True)
    # eventName = fields.Str(required=True)
    # location = fields.Str(required=True)
    # time = fields.DateTime(required=True, data_key="eventTime")
    # isUsed = fields.Bool(dump_only=True)

    time = auto_field(required=True, format="iso")
      
    # @validates_schema
    def validate_time(self, data):
        if 'time' in data:
            event_time = data['time']
            now = utc_now()
   
            if data.get('location') == 'Jakarta':
                # Convert Jakarta time to UTC by subtracting 7 hours
                event_time = event_time - timedelta(hours=7)

            if event_time <= now:
                raise ValidationError("Event time must be in the future. Jakarta events must be in local time.")
        
ticket_schema = TicketSchema()