import json
from pathlib import Path
import requests

BASE_DIR = Path.cwd().resolve()

DATASET_PATH = (BASE_DIR / "data_src/chicago_libraries/dataset").resolve()
METADATA_PATH = (BASE_DIR / "data_src/chicago_libraries/metadata.csv").resolve()

payload = {
    "dataset_name": "chicago_libraries",
    "connector_config": {
        "directory_path": str(DATASET_PATH),
        "metadata_path": str(METADATA_PATH),
        "type": "csv",
    },
    "overwrite": False,
    "schema_summaries": None,
}

response = requests.post("http://localhost:8000/index", json=payload)
print(response.status_code)
print(json.dumps(response.json(), indent=2))