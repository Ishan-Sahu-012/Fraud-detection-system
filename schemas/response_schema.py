from pydantic import BaseModel

class EmailResponse(BaseModel):
    result:str
    score:int
    reasons:list[str]