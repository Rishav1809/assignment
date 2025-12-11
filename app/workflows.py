from app.engine import register_workflow, execute, get_run_state

def sample_workflow(data: dict):
    name = data.get("name", "unknown")
    return {"message": f"Hello, {name}! Your workflow ran successfully."}

def register_workflows():
    register_workflow("greet_user", sample_workflow)

def run_workflow(workflow_name: str, data: dict):
    return execute(workflow_name, data)

def get_state(run_id: str):
    return get_run_state(run_id)

