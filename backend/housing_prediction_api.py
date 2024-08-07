import csv
import datetime
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
import joblib
import pandas as pd
from pydantic import BaseModel

from predictions_table import display_table

# Initialize FastAPI app
app = FastAPI()

# Load the model which is already trained
MODEL_NAME = 'model.joblib'


class HousingParameters(BaseModel):
    """ Pydantic model """
    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: float
    population: float
    households: float
    median_income: float
    ocean_proximity: str


@app.get("/")
def read_root():
    """ Root url """
    try:
        return FileResponse("../frontend/root.html")

    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/housing")
def read_housing_parameters():
    """ Display form to capture inputs """
    try:
        return FileResponse("../frontend/housing_prediction_form.html")
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/predict")
async def predict_house_price(data: HousingParameters):
    """ Perform prediction and return predicted value """

    try:
        dataframe = pd.DataFrame([data.dict()])
        encode_df = pd.get_dummies(dataframe)

        expected_columns = [
            'longitude', 'latitude', 'housing_median_age', 'total_rooms',
            'total_bedrooms', 'population', 'households', 'median_income',
            'ocean_proximity_<1H OCEAN', 'ocean_proximity_INLAND',
            'ocean_proximity_ISLAND', 'ocean_proximity_NEAR BAY',
            'ocean_proximity_NEAR OCEAN'
        ]

        # Reindex the final DataFrame to ensure it has all expected columns
        df_final = encode_df.reindex(columns=expected_columns, fill_value=0)
        model = joblib.load(MODEL_NAME)
        pred = model.predict(df_final)[0]

        dataframe["predicted_price"] = pred
        dataframe["timestamp"] = datetime.datetime.now()

        # Save history of predictions in the prediction table csv
        with open('../data/predictions_table.csv', "a") as file:
            writer = csv.writer(file)
            writer.writerow(dataframe.values[:1][0])

        return pred

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history")
def display_predictions():
    """ Display history of predictions """
    try:
        html_content = display_table()
        return HTMLResponse(html_content)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/graph")
async def get_bar_graph():
    """ Serve the image file """
    try:
        return FileResponse('../data/graph.png', media_type='image/png')
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
