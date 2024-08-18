# Summer Break Tax Report

This is a simple web service API that helps process income and expense data for tax purposes. It allows users to upload transaction data and generate reports. The system is designed to handle transactions, validate their data, and provide meaningful financial reports.

## Setup and Running

### Prerequisites
- Python 3.8 or higher
- Pip (Python package installer)

### Setup
1. Create a virtual environment
```bash
python -m venv venv
```

2. Activate the Virtual Environment

mac/linux
```bash
source venv/bin/activate
```

windows
```bash
venv\Scripts\activate
```
3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Setup Environment Variables in root folder (.env)
```bash
FLASK_ENV=development
FLASK_APP=app
PORT=5000
```

### Running the Application

```bash
python run.py
```
The application will start at `http://127.0.0.1:5000`.

#### Access Endpoints:

- Upload Transactions: POST /transactions
- Generate Report: GET /report

## Solution Approach and Assumptions
- **Data Validation**: The solution uses a schema-based approach to validate transaction data. It ensures that transaction entries conform to expected formats.
- **File Handling**: The solution handles file uploads and filters out comments from the CSV data.
- **Error Handling**: Basic error handling is included to manage invalid transactions and file upload issues.
- **Database**: The current implementation assumes an in-memory database or a simple repository pattern. In a production environment, I might integrate with a relational database.

## Shortcomings of the Solution
- **Validation Coverage**: The validation checks are basic and might need enhancement to cover more edge cases and data integrity rules.
- **Error Handling**: The error handling could be more robust, especially around file parsing and database operations.
- **Testing**: The testing framework setup is minimal. Comprehensive test cases are needed to ensure the robustness of the application.
- **Scalability**: The current implementation is not optimized for large-scale data handling. Performance considerations for large CSV files and high transaction volumes are not addressed.

## Future Improvements
- **Enhanced Validation**: Improve data validation to cover more edge cases, such as handling different date formats or validating numerical ranges.
- **Error Handling**: Implement more detailed error handling and logging to better diagnose and manage issues.
- **Database Integration**: Integrate a robust database system with ORM (Object-Relational Mapping) to handle persistent storage.
- **Testing**: Expand test coverage to include unit tests, integration tests, and performance tests.
- **User Authentication**: Add user authentication and authorization to secure access to endpoints and protect sensitive data.
    - **Sessions**: Implement user authentication to manage user sessions. Users should be able to log in and out of the system securely.
    - **Authorization**: Ensure that users can only access and manage their own data. This will involve:
        - Adding user models and authentication mechanisms (e.g., JWT tokens, OAuth).
        - Implementing role-based or attribute-based access controls.
        - Securing endpoints to ensure users can only perform actions on their own data.
- **Documentation**: Enhance the documentation to include detailed API specifications and usage examples.
