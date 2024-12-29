---
title: Text Captcha Breaker
emoji: 🏃
colorFrom: indigo
colorTo: gray
sdk: gradio
sdk_version: 4.42.0
app_file: app.py
pinned: false
license: GPL-v3
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# Text Captcha Breaker

- Original project [here](https://huggingface.co/spaces/docparser/Text_Captcha_breaker/tree/main).
- There are some minor changes for usability in the wild.
- Many thanks to the original developer for providing the perfectly trained file for its purpose.

## Usage

- Clone this repository on your project's directory:

```bash
cd <your_project_dir>
git clone https://github.com/mybotsss/Text_Captcha_Breaker.git
# Check file size of captcha.onnx (It has to be: ~90MB)
# Install requirments
python3 -m pip install -r Text_Captcha_Breaker/requirements.txt
```

- Call and use the function as below:

```python
from Text_Captcha_Breaker.app import get_text

input_path = "/path/to/image.png"
text,_ = get_text(image_path)
print(f"Result: {text}")
```

- Check `ex_usage.py` file.

## API Serve

- If you want to use the interface and API similar to [Hugging Face](https://huggingface.co/spaces/docparser/Text_Captcha_breaker), uncomment the `gr.Interface` section in `Text_Captcha_Breaker.app`.

`python3 -m pip install gradio`
