import gradio as gr
import requests
import numpy as np

# def predict(img):
#     # Convert PIL Image to numpy array
#     img_array = np.array(img, dtype=np.uint8)  # Ensure the array is of type uint8
    
#     # Ensure the array is in the correct format (list of lists of integers)
#     payload = {"array": img_array.tolist()}
    
#     # Make the POST request to the FastAPI endpoint
#     response = requests.post("http://0.0.0.0:8000/predict", json=payload)
    
#     if response.status_code == 200:
#         prediction = response.json().get("prediction")
#         return f"The patient {prediction}"
#     else:
#         return "Error in prediction"

def predict(img):
    # Convert PIL Image to numpy array
    img_array = np.array(img, dtype=np.uint8)  # Ensure the array is of type uint8
    
    # Ensure the array is in the correct format (list of lists of integers)
    payload = {"array": img_array.tolist()}
    
    # Make the POST request to the FastAPI endpoint
    response = requests.post("http://fastapi-app:8000/predict", json=payload)
    
    if response.status_code == 200:
        prediction = response.json().get("prediction")
        return f"The patient {prediction}"
    else:
        return "Failed to get prediction"

# Create the Gradio interface
demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(image_mode='RGB'),
    outputs=gr.Textbox(label="Status of patient")
)

# Launch the Gradio interface
demo.launch()