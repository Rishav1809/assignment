import uuid
from typing import Callable, Dict

RUNS: Dict[str, dict] = {}     # in-memory state
WORKFLOWS: Dict[str, Callable] = {}

def register_workflow(name: str, func: Callable):
    WORKFLOWS[name] = func

def execute(name: str, data: dict):
    run_id = str(uuid.uuid4())

    if name not in WORKFLOWS:
        return {"error": "workflow not found"}

    try:
        output = WORKFLOWS[name](data)
        RUNS[run_id] = {"status": "completed", "output": output}
    except Exception as e:
        RUNS[run_id] = {"status": "failed", "error": str(e)}

    return {"run_id": run_id}

def get_run_state(run_id: str):
    return RUNS.get(run_id, {"error": "run_id not found"})
