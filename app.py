import numpy as np
import timm
import torch
from flask import Flask, jsonify, render_template, request
from huggingface_hub import hf_hub_download
from PIL import Image

from advice import LABELS, build

REPO = "kssrikar4/Rice-Leaf-Disease-Classification"  # pretrained rice model, used as-is
THRESHOLD = 0.60  # below this -> "no clear disease"

torch.set_num_threads(2)  # light on CPU

weights = hf_hub_download(REPO, "rice_model.pth")
state = torch.load(weights, map_location="cpu", weights_only=True)
n = state["head.fc.weight"].shape[0]  # 7 in this checkpoint
model = timm.create_model("swin_tiny_patch4_window7_224", pretrained=False, num_classes=n)
model.load_state_dict(state)
model.eval()

MEAN = np.array([0.485, 0.456, 0.406], dtype=np.float32)
STD = np.array([0.229, 0.224, 0.225], dtype=np.float32)

app = Flask(__name__)


def preprocess(img: Image.Image) -> torch.Tensor:
    img = img.convert("RGB").resize((224, 224), Image.BILINEAR)
    x = (np.asarray(img, dtype=np.float32) / 255.0 - MEAN) / STD
    return torch.from_numpy(x).permute(2, 0, 1).unsqueeze(0)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    img = Image.open(request.files["image"].stream)
    with torch.no_grad():
        probs = torch.softmax(model(preprocess(img)), dim=1)[0]

    top_p, top_i = probs.max(dim=0)
    label = LABELS[top_i.item()] if top_p.item() >= THRESHOLD else None

    result = build(label)
    result["confidence"] = round(top_p.item() * 100, 1)
    order = probs.argsort(descending=True)[:3]
    result["top3"] = [{"label": LABELS[i], "score": round(probs[i].item() * 100, 1)} for i in order.tolist()]
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=False, port=5000)
