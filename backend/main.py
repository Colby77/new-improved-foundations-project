"""
The main file for the FastAPI backend

Run the server with:
    'uvicorn main:app --reload'
"""

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {"Message": {
                "Hello": "World",
                "Testing": "123"
            }
        }

