from pydantic import BaseModel

class WorkflowRequest(BaseModel):
    workflow_name: str
    input_data: dict

class WorkflowRunResponse(BaseModel):
    run_id: str
