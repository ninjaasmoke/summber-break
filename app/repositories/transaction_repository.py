class TransactionRepository:
    _transactions = []

    @staticmethod
    def save_transactions(transactions):
        TransactionRepository._transactions.extend(transactions)

    @staticmethod
    def calculate_totals():
        gross_revenue = sum(t['amount'] for t in TransactionRepository._transactions if t['type'] == 'Income')
        total_expenses = sum(t['amount'] for t in TransactionRepository._transactions if t['type'] == 'Expense')
        return gross_revenue, total_expenses
