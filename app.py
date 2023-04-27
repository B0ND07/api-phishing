

import uvicorn
from fastapi import FastAPI
from UrlData import UrlData
from API import get_prediction
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ------------------------------------------

# Enabling CORS policy

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------

model_path = r"Malicious_URL_Prediction.h5"

# passing variables to ML model to return prediction
# NOTE : the request is POST
@app.post("/predict")
def predict(data: UrlData):

    # convert to dictionary
    data = data.dict()

    # the key has same name as you put in HouseData class
    url = data["url"]


    # predict price
    prediction = get_prediction(url,model_path)
    print("Predicted Probability : ",prediction)

    # always return the output as dictionary/json.
    # It's better if your output is a string.
    prediction = {"prediction": str(prediction)}

    return prediction






















