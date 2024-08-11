import requests

ENDPOINT = "http://127.0.0.1:8000"

def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    

def test_can_create_task():
    payload = {
        "type": "LONG", 
        "tradedate": "2024-07-31T21:35:44.247Z",
        "entry_price": 3000,
        "exit_price": 3100,
        "quantity": 2,
        "TP": 3100,
        "SL": 2950,
        "ratio": 1,
        "profit": 100,
        "notes": "Pytest Weekly Bias Strat"
    }
    response = requests.post(ENDPOINT + "/trades/ETHUSD/2024-07-22", json=payload)
    assert response.status_code == 200

    data = response.json()
    print(data)