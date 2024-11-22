# Import necessary modules
from fastapi import FastAPI
from pydantic import BaseModel
import logging

# Initialize FastAPI app
app = FastAPI()

# Configure logging for debugging
logging.basicConfig(level=logging.INFO)

# Define request model for input validation
class CalculationRequest(BaseModel):
    number1: float
    number2: float

# Endpoint for addition
@app.post("/add")
def add_numbers(request: CalculationRequest):
    result = request.number1 + request.number2
    logging.info(f"Addition: {request.number1} + {request.number2} = {result}")
    return {"operation": "addition", "result": result}

# Endpoint for multiplication
@app.post("/multiply")
def multiply_numbers(request: CalculationRequest):
    result = request.number1 * request.number2
    logging.info(f"Multiplication: {request.number1} * {request.number2} = {result}")
    return {"operation": "multiplication", "result": result}