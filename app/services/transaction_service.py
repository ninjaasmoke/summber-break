from flask import jsonify
from app.repositories import TransactionRepository
from app.schemas import TransactionSchema
import csv
import io

class TransactionService:
    @staticmethod
    def upload_transactions(request):
        file = request.files.get('data')
        if not file and not data:
            return jsonify({"error": "No file provided"}), 400

        try:
            # read the file content into a string
            file_content = io.StringIO(file.stream.read().decode("UTF8")).getvalue()
            lines = file_content.splitlines()

            # filter out lines that start with a comment character
            filtered_lines = [line for line in lines if not line.strip().startswith('#')]

            # create a StringIO object with the filtered lines
            stream = io.StringIO("\n".join(filtered_lines))

            # parse the CSV content
            csv_input = csv.DictReader(stream, fieldnames=["Date", "Type", "Amount($)", "Description"])

            # validate and process transactions
            transactions = []
            for row in csv_input:
                if any(value.strip() == '' for value in row.values()):
                    continue  # skip rows with missing values
                try:
                    validated_transaction = TransactionSchema.validate(row)
                    transactions.append(validated_transaction)
                except ValueError as e:
                    # continue to skip invalid transactions?
                    # print(f"Skipping invalid transaction: {e}")
                    return jsonify({"error": str(e)}), 400

            # save transactions to the repository
            TransactionRepository.save_transactions(transactions)
            return jsonify({"message": "Transactions uploaded successfully"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def generate_report():
        gross_revenue, total_expenses = TransactionRepository.calculate_totals()
        net_revenue = gross_revenue - total_expenses
        gross_revenue = round(gross_revenue, 2)
        total_expenses = round(total_expenses, 2)
        net_revenue = round(net_revenue, 2)
        return jsonify({
            "gross-revenue": gross_revenue,
            "expenses": total_expenses,
            "net-revenue": net_revenue
        })
