from pathlib import Path
import json
p = Path.cwd() / "history.json"
def read_history():
    with open(p, "r") as f:
        return json.load(f)
    
print(read_history())