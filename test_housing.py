import pytest
from housing_prices_dashboard.housing_prediction_api import predict_house_price, app
from fastapi.testclient import TestClient


class TestHousingPrediction:
    def test_predict_house_price(self):
        input_1 = {
            "longitude": -118.24,
            "latitude": 34.12,
            "housing_median_age": 30,
            "total_rooms": 1000,
            "total_bedrooms": 200,
            "population": 5000,
            "households": 1500,
            "median_income": 3.5,
            "ocean_proximity": "<1H OCEAN"
        }

        input_2 = {"longitude": -115.73,
                   "latitude": 33.35,
                   "housing_median_age": 23.0,
                   "total_rooms": 1586.0,
                   "total_bedrooms": 448.0,
                   "population": 338.0,
                   "households": 182.0,
                   "median_income": 1.2132,
                   "ocean_proximity": 'INLAND'}

        input_3 = {"longitude": -117.96,
                   "latitude": 33.89,
                   "housing_median_age": 24.0,
                   "total_rooms": 1332.0,
                   "total_bedrooms": 252.0,
                   "population": 625.0,
                   "households": 230.0,
                   "median_income": 4.4375,
                   "ocean_proximity": '<1H OCEAN'}

        assert predict_house_price(input_1) == 320201.58554044
        assert predict_house_price(input_2) == 58815.45033765
        assert predict_house_price(input_3) == 192575.77355635


@pytest.fixture(scope="module")
def client():
    yield TestClient(app)

def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "json" in response.headers["content-type"]


def test_read_housing_parameters(client):
    response = client.get("/housing")
    assert response.status_code == 200
    assert isinstance(response.json(), list)





