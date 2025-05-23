#!/usr/bin/python

#!pip install spacy fastapi

from fastapi import FastAPI, Body
import uvicorn
from pydantic import BaseModel

# create the webapp.
app = FastAPI(title="My First REST API Server")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q:str=None):
    return {"item_id": item_id, "q": q}

class Data(BaseModel):
    text:str
    lang:str

@app.post("/text/")
def extract_entities(data:Data, query:str):
    found = query in data.text
    return {"message": data.text, "query":query, "found":found}

@app.post("/bodytext")
async def extract_body(data:str=Body(...), query:str=""):
    found = query in data if query != "" else False
    return {"bodytext":data, "query":query, "found":found}

# Run from command line: uvicorn apiWithBody:app --port 7000 --host 0.0.0.0
# or invoke the code below.
uvicorn.run(app, host='0.0.0.0', port=7000)