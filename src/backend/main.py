# =============================================================================
# SETUP
import json

from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# =============================================================================
# CORS

origins = [
    "http://localhost:5173",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =============================================================================
# API Endpoints

@app.get("/")
def read_root():
    """
    Root endpoint of the API.
    Returns a JSON response with a greeting message.
    """
    return {"Hello": "World"}


@app.get("/data/read_nodes")
async def read_nodes(id: str | None = None):
    """
    Endpoint to read D3.js data.
    Reads the JSON data from a file based on the provided data_id.
    Returns the JSON data as a response.
    If the file is not found, returns an error message.
    """
    try:
        with open(f"./ipynb/{id}/{id}_D3.json", "r") as file:
            nodes = json.load(file)
        return nodes
    
    except FileNotFoundError:
        return {"error": "File not found."}
    

# @app.post("/data/mianInfo={data_id}")
# async def read_mianInfo()

@app.get("/data/mianInfo")
async def read_items(id: str | None = None):

    try:
        with open(f"./ipynb/{id}/{id}_mianInfo.json", "r") as file:
            mianInfo = json.load(file)
        return mianInfo
    
    except FileNotFoundError:
        return {"error": f"File not foundd."}
