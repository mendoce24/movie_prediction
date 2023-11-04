from fastapi import FastAPI, HTTPException
import pandas as pd
from movie import ratings
import datetime

app = FastAPI()

@app.get('/')
def index():
    return "API to predict recomendation of movies."

@app.get('/predict')
def read_item():
    mov = ratings(1,1,4.5,datetime.datetime.now())
    mov_data = mov.json_structure()
    return mov_data

def update_item(item: ratings):

    immo = item #Preprocessing().transform_data_api(item)

    validate_data(immo)

    value_to_return = immo #Predict().get_price_api(immo)

    return (value_to_return)


def validate_data(immo):
    if ((pd.api.types.is_numeric_dtype(immo.constructionYear)) &
        pd.api.types.is_numeric_dtype(immo.netHabitableSurface)) == False:
        raise HTTPException(status_code=404, detail='expected numbers, got strings.')
    