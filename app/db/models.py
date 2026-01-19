from pydantic import BaseModel, conint
from typing import List

class Answer(BaseModel):
    question_id: conint(ge=0, le=2147483647)
    alternative_id: conint(ge=0, le=2147483647)

class UserAnswer(BaseModel):
    user_id: conint(ge=0, le=2147483647)
    answers: List[Answer]