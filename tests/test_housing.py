from housing_prices_dashboard.backend.housing_prediction_api import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "<title>Root Page</title>" in response.text

def test_read_housing_parameters():
    response = client.get("/housing")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "<form" in response.text

def test_predict_house_price(housing_parameters):
    response = client.post("/predict", json=housing_parameters)
    assert response.status_code == 200
    assert round(response.json(), 8) == 320201.58554044
    print("res", response.json())

def test_display_predictions():
    response = client.get("/history")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "<title>Predictions History</title>" in response.text

def test_get_bar_graph():
    response = client.get("/graph")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"