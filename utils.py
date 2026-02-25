import json

def safe_json_load(content):
    try:
        return json.loads(content)
    except Exception:
        return None
