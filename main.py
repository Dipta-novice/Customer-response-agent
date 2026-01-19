from fastapi import FastAPI
from pydantic import BaseModel
from agent import handle_customer_email

app = FastAPI()

class EmailInput(BaseModel):
    email: str

@app.post("/handle-email")
def process_email(data: EmailInput):
    result = handle_customer_email(data.email)
    return {"result": result}
