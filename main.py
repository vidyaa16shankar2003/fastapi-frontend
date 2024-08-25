# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()

class DataModel(BaseModel):
    data: List[Union[str, int]]

@app.post("/bfhl")
async def process_data(request: DataModel):
    user_id = "vidyaa_shankar_16082003"
    email = "vidyaashankar.m2021@vitstudent.ac.in"
    roll_number = "21BCE1061"

    numbers = [str(item) for item in request.data if str(item).isdigit()]
    alphabets = [str(item) for item in request.data if str(item).isalpha()]
    lowercase_alphabets = [item for item in alphabets if item.islower()]

    highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else ""

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
    }
    return response

@app.get("/bfhl")
async def get_operation_code():
    return {"operation_code": 1}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
