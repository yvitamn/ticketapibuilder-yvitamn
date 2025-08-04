from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from models.ticket_model import Ticket
from schemas.ticket_schema import TicketSchema
from services.ticket_service import (
    get_all_tickets,
    get_ticket_by_id,
    create_ticket,
    delete_ticket,
    mark_ticket_used
)
from shared.error_handlers import format_response, handle_error


ticket_bp = Blueprint("tickets", __name__)
ticket_schema = TicketSchema()


@ticket_bp.route("/", methods=["GET"])
def get_all():
    tickets = get_all_tickets()
    return format_response(tickets)

@ticket_bp.route("/<int:ticket_id>", methods=["GET"])
def get_one(ticket_id):
    ticket = get_ticket_by_id(ticket_id)
    return format_response(ticket)

@ticket_bp.route("/", methods=["POST"])
def create():
    data = request.get_json()
    
    try:
        print("Received data:", data)
        ticket = create_ticket(data)
        return format_response(ticket_schema.dump(ticket), status_code=201)
    except Exception as e:
        print("Exception in /tickets:", e)
        return handle_error(str(e), 400)
    
@ticket_bp.route("/<int:ticket_id>", methods=["PATCH"])
def mark_used(ticket_id):
    ticket = mark_ticket_used(ticket_id)
    return format_response(ticket)

@ticket_bp.route("/<int:ticket_id>", methods=["DELETE"])
def delete(ticket_id):
    result = delete_ticket(ticket_id)
    return format_response(result)
