import csv
from typing import List, Dict

class TransactionSchema:
    @staticmethod
    def validate(transaction: Dict[str, str]) -> Dict[str, any]:
        # check for valid format
        if len(transaction) != 4:
            raise ValueError("Invalid transaction format: Expected 4 fields")
        
        date, trans_type, amount, description = transaction.values()
        
        # validate date
        try:
            date_parts = date.split('-')
            if len(date_parts) != 3 or not all(part.isdigit() for part in date_parts):
                raise ValueError("Invalid date format")
        except Exception as e:
            raise ValueError(f"Invalid date: {e}")

        # validate amount
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError("Invalid amount format")

        # validate type
        trans_type = trans_type.strip()  # strip any extra whitespace
        if trans_type not in {"Income", "Expense"}:
            raise ValueError(f"Invalid transaction type: {trans_type}")
        
        # return validated transaction
        return {
            "date": date,
            "type": trans_type,
            "amount": amount,
            "description": description
        }
