---
title: Text Captcha Breaker
emoji: 🏃
colorFrom: indigo
colorTo: gray
sdk: gradio
sdk_version: 4.42.0
app_file: app.py
pinned: false
license: apache-2.0
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# Text Captcha Breaker

- Original project [here](https://huggingface.co/spaces/docparser/Text_Captcha_breaker/tree/main).
- There are some minor changes for usability in the wild.
- Many thanks to the original developer for providing the perfectly trained file for its purpose.

## Usage

- Clone this project on your project's directory:

```bash
# Clone this repository into your project directory
cd <your_project_dir>
git clone https://github.com/mybotsss/Text_Captcha_Breaker.git
# Check file size of captcha.onnx (It has to be: ~90MB)
# Install requirments
python3 -m pip install -r Text_Captcha_Breaker/requirements.txt
```

- Call and use the function as below:

```python
from Text_Captcha_Breaker.app import get_text

input_path = os.path.join(input_directory, filename)
text,_ = get_text(image_path)
print(f"Result: {text}")
```

- Check `ex_usage.py` file.
