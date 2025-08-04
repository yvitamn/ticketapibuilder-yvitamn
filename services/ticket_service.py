from flask import abort
from instance.database import db
from models.ticket_model import Ticket
from repos.ticket_repo import TicketRepository
from schemas.ticket_schema import TicketSchema
from marshmallow import ValidationError

ticket_repo = TicketRepository()
ticket_schema = TicketSchema() #validating one ticket
ticket_list_schema = TicketSchema(many=True) #validating multiple tickets

def get_all_tickets():
    tickets = ticket_repo.get_all()
    return ticket_list_schema.dump(tickets)

def get_ticket_by_id(ticket_id: int):
    ticket = ticket_repo.get_by_id(ticket_id)
    if not ticket:
        abort(404, "Ticket not found")
    return ticket_schema.dump(ticket)

def create_ticket(data: dict):
    # load = validate + create instance
    ticket = ticket_schema.load(data)
    db.session.add(ticket)
    db.session.commit()
    return ticket
    

def mark_ticket_used(ticket_id):
    ticket = ticket_repo.get_by_id(ticket_id)
    if not ticket:
        abort(404, "Ticket not found")
    ticket.isUsed = True
    db.session.commit()
    return ticket_schema.dump(ticket)

def delete_ticket(ticket_id):
    ticket = ticket_repo.get_by_id(ticket_id)
    if not ticket:
        abort(404, "Ticket not found")
    ticket_repo.delete(ticket)
    return {"message": "Ticket deleted successfully"}
