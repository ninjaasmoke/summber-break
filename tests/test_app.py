import pytest
from app import create_app
from io import BytesIO

@pytest.fixture
def client():
    # create an app instance using the factory function
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_transactions_and_report(client):
    # prepare test data for the first upload
    data_csv_1 = b"2020-07-01,Expense,18.77,Gas\n2020-07-04,Income,40.00,347 Woodrow"
    data_csv_2 = b"2020-07-05,Expense,30.00,Electricity\n2020-07-06,Income,60.00,Job"

    # upload first CSV file
    rv = client.post('/transactions', data={'data': (BytesIO(data_csv_1), 'data1.csv')})
    assert rv.status_code == 201
    assert b"Transactions uploaded successfully" in rv.data

    # Get the report after the first upload
    rv = client.get('/report')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data['expenses'] == 18.77
    assert json_data['gross-revenue'] == 40.0
    assert json_data['net-revenue'] == pytest.approx(21.23)

    # Upload second CSV file
    rv = client.post('/transactions', data={'data': (BytesIO(data_csv_2), 'data2.csv')})
    assert rv.status_code == 201
    assert b"Transactions uploaded successfully" in rv.data

    # Get the report after the second upload
    rv = client.get('/report')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data['expenses'] == 48.77
    assert json_data['gross-revenue'] == 100.0
    assert json_data['net-revenue'] == pytest.approx(51.23)

def test_invalid_csv(client):
    data_invalid_csv = b"2020-07-01,Invalid,18.77,Gas"
    rv = client.post('/transactions', data={'data': (BytesIO(data_invalid_csv), 'invalid.csv')})
    assert rv.status_code == 400
    assert b"Invalid transaction type" in rv.data
