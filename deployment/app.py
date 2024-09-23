from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
from typing import List
from src.main import make_prediction

app = FastAPI()

class ImageData(BaseModel):
    array: List[List[List[int]]]  

@app.post("/predict")
async def predict(image_data: ImageData):

    # Convert list to numpy array
    np_array = np.array(image_data.array)
    # Get prediction from model
    prediction = make_prediction(np_array)
    return {"prediction": prediction}

@app.get("/model_info")
async def model_info():
    # Return dummy model info
    return {"model_name": "SimpleVGG", "version": "1.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)