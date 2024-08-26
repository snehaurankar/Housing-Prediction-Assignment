import pytest

@pytest.fixture()
def housing_parameters():
    """ Generate a set of housing parameters for testing """
    return {
        "longitude": -122.64,
        "latitude": 38.01,
        "housing_median_age": 36.0,
        "total_rooms": 1336.0,
        "total_bedrooms": 258.0,
        "population": 678.0,
        "households": 249.0,
        "median_income": 5.5789,
        "ocean_proximity": 'NEAR OCEAN'
    }