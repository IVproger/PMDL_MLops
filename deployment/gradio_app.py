import gradio as gr
from src.main import make_prediction

def predict(img):
    prediction = make_prediction(img=img)
    return f"The patient {prediction}"

# Create the Gradio interface
demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(image_mode='RGB'),
    outputs=gr.Textbox(label="Status of patient")
)

# Launch the Gradio interface
demo.launch()