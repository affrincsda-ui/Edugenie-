
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0"
)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(directory="templates")


class UserInput(BaseModel):
    text: str


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/qa")
def qa(data: UserInput):
    return {"result": answer_question(data.text)}


@app.post("/explain")
def explain(data: UserInput):
    return {"result": explain_topic(data.text)}


@app.post("/quiz")
def quiz(data: UserInput):
    return {"result": generate_quiz(data.text)}


@app.post("/summarize")
def summarize(data: UserInput):
    return {"result": summarize_text(data.text)}


@app.post("/learn/recommendations")
def learn(data: UserInput):
    return {
        "result": get_learning_recommendations(data.text)
    }
  
