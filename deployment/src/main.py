import torch
from torchvision import transforms
import numpy as np
from PIL import Image
from src.model import SimpleVGG

def image_predprocessing(img: np.array):
    
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
    ])
    
    # Convert numpy array to PIL Image
    img = Image.fromarray(img).convert('RGB')
    
    image_tensor = transform(img).unsqueeze(0) 
    
    return image_tensor

def make_prediction(img):
    num_classes = 2
    model_path = './models/baseline_chest_xray.pth'

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    model = SimpleVGG(num_classes=num_classes).to(device)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    
    image_tensor = image_predprocessing(img)
    
    with torch.no_grad():
        output = model(image_tensor.to(device))
        prediction = torch.argmax(output, dim=1).item()
    
    if prediction == 1:
        return "has pneumonia"
    else:
        return "is healthy"