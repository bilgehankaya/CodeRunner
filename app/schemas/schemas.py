from pydantic import BaseModel


class Request(BaseModel):
    code: str
    testInput: str


languages = ("java", "python")
