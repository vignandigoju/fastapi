from fastapi import FastAPI, HTTPException
from starlette.responses import Response
from pydantic import BaseModel, ValidationError

from app.db.models import UserAnswer
from app.api import api

app = FastAPI()


class UserAnswerModel(BaseModel):
    user_id: int
    question_id: int
    answer: str


@app.get("/")
def root():
    return {"message": "Fast API in Python"}


@app.get("/user")
def read_user():
    return api.read_user()


@app.get("/question/{position}", status_code=200)
def read_questions(position: int, response: Response):
    question = api.read_questions(position)

    if not question:
        raise HTTPException(status_code=400, detail="Error")

    return question


@app.get("/alternatives/{question_id}")
def read_alternatives(question_id: int):
    return api.read_alternatives(question_id)


@app.post("/answer", status_code=201)
def create_answer(payload: UserAnswerModel):
    try:
        validated_payload = payload.dict()
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return api.create_answer(validated_payload)


@app.get("/result/{user_id}")
def read_result(user_id: int):
    return api.read_result(user_id)