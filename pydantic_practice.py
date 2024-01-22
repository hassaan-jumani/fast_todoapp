from pydantic import BaseModel

class Todo_pydantic(BaseModel):
    name: str
    description: str
