# ML model version tracker (e.g., MLflow)import os
import json

TRACKING_FILE = "model_versions.json"

def log_model_version(name: str, version: str, path: str):
    if os.path.exists(TRACKING_FILE):
        with open(TRACKING_FILE, "r") as f:
            data = json.load(f)
    else:
        data = {}

    data[name] = {"version": version, "path": path}

    with open(TRACKING_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_model_info(name: str):
    if os.path.exists(TRACKING_FILE):
        with open(TRACKING_FILE, "r") as f:
            data = json.load(f)
        return data.get(name)
    return None
