from flask import Blueprint, request, jsonify
import services.ticket_service as ticket_service

ticket_bp = Blueprint("tickets", __name__, url_prefix="/tickets")

@ticket_bp.route("/", methods=["GET"])
def get_all():
    return jsonify(ticket_service.get_all_tickets())

@ticket_bp.route("/<int:ticket_id>", methods=["GET"])
def get_one(ticket_id):
    return jsonify(ticket_service.get_ticket_by_id(ticket_id))

@ticket_bp.route("/", methods=["POST"])
def create():
    return jsonify(ticket_service.create_ticket(request.json)), 201

@ticket_bp.route("/<int:ticket_id>", methods=["PATCH"])
def mark_used(ticket_id):
    return jsonify(ticket_service.mark_ticket_used(ticket_id))

@ticket_bp.route("/<int:ticket_id>", methods=["DELETE"])
def delete(ticket_id):
    return jsonify(ticket_service.delete_ticket(ticket_id))
