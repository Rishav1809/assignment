from fastapi import FastAPI
from app.workflows import register_workflows, run_workflow, get_state
from app.models import WorkflowRequest, WorkflowRunResponse

app = FastAPI(title="Simple Workflow Engine")

# Register workflows on startup
register_workflows()

@app.post("/run", response_model=WorkflowRunResponse)
def run(req: WorkflowRequest):
    return run_workflow(req.workflow_name, req.input_data)

@app.get("/state/{run_id}")
def state(run_id: str):
    return get_state(run_id)