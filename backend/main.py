from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    message: str

@app.post("/ask")
async def ask(query: Query):
    text = query.message.lower()

    if "exam" in text or "result" in text:
        reply = (
            "Exams can put a lot of pressure on your mind. "
            "It’s normal to feel scared about results. "
            "What do you think is the worst thing that could happen?"
        )

    elif "alone" in text or "lonely" in text:
        reply = (
            "Feeling alone can be very painful. "
            "Even though it feels that way, you are not actually alone right now. "
            "Has this feeling been with you for a long time?"
        )

    elif "bad" in text or "sad" in text:
        reply = (
            "I’m really sorry you’re feeling this way. "
            "Bad feelings can feel heavy, especially under stress. "
            "Would you like to talk about what made today especially hard?"
        )

    else:
        reply = (
            "Thank you for sharing this with me. "
            "I’m here to listen. Can you tell me a bit more?"
        )

    return {
        "response": reply,
        "tool_called": "rule-based"
    }
