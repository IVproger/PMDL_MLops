import torch
import torch.nn as nn

# Model definition
class SimpleVGG(nn.Module):
    def __init__(self, num_classes=2):
        super(SimpleVGG, self).__init__()
        
        # Define 1 VGG block
        self.block1 = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        
        # Define the classifier
        self.classifier = nn.Sequential(
            nn.Linear(16 * 128 * 128, 128),  # Adjusted input size
            nn.ReLU(inplace=True),
            nn.Dropout(),
            nn.Linear(128, num_classes)
        )
    
    def forward(self, x):
        x = self.block1(x)
        x = x.view(x.size(0), -1)  # Flatten the tensor
        x = self.classifier(x)
        return x