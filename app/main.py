"""
This module is the main module for the FastAPI app.
"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

from fastapi import FastAPI

from .routers import api


# --------------------------------------------------------------------------------
# App Creation
# --------------------------------------------------------------------------------

app = FastAPI()
app.include_router(api.router)


# --------------------------------------------------------------------------------
# Routes
# --------------------------------------------------------------------------------

@app.get("/")
def read_root():
  return {"Hello": "World"}
