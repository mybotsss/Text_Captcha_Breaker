import torch
import onnx
import onnxruntime as rt
from torchvision import transforms as T
from PIL import Image
from .tokenizer_base import Tokenizer
import os
#import gradio as gr


current_dir = os.path.dirname(__file__)
model_file = os.path.join(current_dir, 'captcha.onnx')
img_size = (32,128)
charset = r"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
tokenizer_base = Tokenizer(charset)

def get_transform(img_size):
        transforms = []
        transforms.extend([
            T.Resize(img_size, T.InterpolationMode.BICUBIC),
            T.ToTensor(),
            T.Normalize(0.5, 0.5)
        ])
        return T.Compose(transforms)

def to_numpy(tensor):
    return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()

def initialize_model(model_file):
    transform = get_transform(img_size)
    # Onnx model loading
    onnx_model = onnx.load(model_file)
    onnx.checker.check_model(onnx_model)
    ort_session = rt.InferenceSession(model_file)
    return transform,ort_session 

def get_text(image_path):
    img = Image.open(image_path)
    # Preprocess. Model expects a batch of images with shape: (B, C, H, W)
    x = transform(img.convert('RGB')).unsqueeze(0)

    # compute ONNX Runtime output prediction
    ort_inputs = {ort_session.get_inputs()[0].name: to_numpy(x)}
    logits = ort_session.run(None, ort_inputs)[0]
    probs = torch.tensor(logits).softmax(-1)
    preds, probs = tokenizer_base.decode(probs)
    return preds[0], probs

transform,ort_session = initialize_model(model_file=model_file)

# gr.Interface(
#     get_text,
#     inputs=gr.Image(type="pil"),
#     outputs=gr.Textbox(),
#     title="Text Captcha Reader",
#     examples=["images/8000.png","images/11JW29.png","images/2a8486.jpg","images/2nbcx.png",
#              "000679.png","images/000HU.png","images/00Uga.png.jpg","images/00bAQwhAZU.jpg",
#              "00h57kYf.jpg","images/0EoHdtVb.png","images/0JS21.png","images/0p98z.png","images/10010.png"]
# ).launch()

# if __name__ == "__main__":
#     image_path = "images/8000.png"
#     text,_ = get_text(image_path)
#     print(text)
