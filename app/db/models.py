from pydantic import BaseModel, conint, validator
from typing import List
import re

class Answer(BaseModel):
    question_id: conint(ge=0, le=2147483647)
    alternative_id: conint(ge=0, le=2147483647)

    @validator('question_id', 'alternative_id')
    def validate_ids(cls, v):
        if not re.match(r'^\d+$', str(v)):
            raise ValueError('ID must be a positive integer')
        return v

class UserAnswer(BaseModel):
    user_id: conint(ge=0, le=2147483647)
    answers: List[Answer]

    @validator('user_id')
    def validate_user_id(cls, v):
        if not re.match(r'^\d+$', str(v)):
            raise ValueError('User ID must be a positive integer')
        return v