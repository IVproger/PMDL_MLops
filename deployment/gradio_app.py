import gradio as gr
from src.main import make_prediction

def predict(img):
    
    prediction = make_prediction(img=img)
    
    return f"The patient {prediction}"
    

demo = gr.Interface(fn=predict, inputs=gr.Image(image_mode='RGB'), outputs="text")

demo.launch()