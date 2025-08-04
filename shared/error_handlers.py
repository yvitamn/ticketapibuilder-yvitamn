import traceback
from flask import jsonify

def format_response(data=None, success=True, status_code=200):
    """Standard response formatter for all endpoints"""
    if data is None:
        data = {}
        
    return jsonify({
        "data": data,
        "success": success
    }), status_code

def handle_error(message, status_code):
    """Error response formatter"""
    traceback.print_exc()
    return jsonify({
        "data": {
            "message": message
        },
        "success": False
    }), status_code

def register_error_handlers(app):
    @app.errorhandler(400)
    def handle_400_error(e):
        return jsonify({"error": "Bad Request", "message": str(e)}), 400

    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify({"error": "Not Found", "message": str(e)}), 404

    @app.errorhandler(500)
    def handle_500_error(e):
        return jsonify({"error": "Internal Server Error", "message": "Something went wrong"}), 500
