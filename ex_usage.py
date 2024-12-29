import os
from Text_Captcha_Breaker.app import get_text


# Process all image files in the 'images' directory
input_directory = 'images'
output_directory = 'processed_images'
os.makedirs(output_directory, exist_ok=True)

for filename in os.listdir(input_directory):
    if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
        input_path = os.path.join(input_directory, filename)
        text,_ = get_text(input_path)
        print(f"{filename}: {text}")
