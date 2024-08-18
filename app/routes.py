from flask import request, jsonify
from app.models import Transaction
from app.services.transaction_service import TransactionService

def init_routes(app):
    @app.route('/transactions', methods=['POST'])
    def upload_transactions():
        return TransactionService.upload_transactions(request)

    @app.route('/report', methods=['GET'])
    def report():
        return TransactionService.generate_report()