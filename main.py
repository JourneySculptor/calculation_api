# Import necessary modules
from fastapi import FastAPI
from pydantic import BaseModel
import logging
import math

# Initialize FastAPI app
app = FastAPI()

# Configure logging for debugging
logging.basicConfig(level=logging.INFO)

# Define request model for input validation
class CalculationRequest(BaseModel):
    number1: float
    number2: float

# Define request model for operations requiring a single number
class SingleNumberRequest(BaseModel):
    number1: float

# Initialize history list
history = []

# Add calculation to history
def add_to_history(operation: str, result: float):
    history.append({"operation": operation, "result": result})

# Endpoint for addition
@app.post("/add")
def add_numbers(request: CalculationRequest):
    result = request.number1 + request.number2
    logging.info(f"Addition: {request.number1} + {request.number2} = {result}")
    add_to_history("addition", result)
    return {"operation": "addition", "result": result}

# Endpoint for subtraction
@app.post("/subtract")
def subtract_numbers(request: CalculationRequest):
    result = request.number1 - request.number2
    logging.info(f"Subtraction: {request.number1} - {request.number2} = {result}")
    add_to_history("subtract", result)
    return {"operation": "subtraction", "result": result}

# Endpoint for multiplication
@app.post("/multiply")
def multiply_numbers(request: CalculationRequest):
    result = request.number1 * request.number2
    logging.info(f"Multiplication: {request.number1} * {request.number2} = {result}")
    add_to_history("multiply", result)
    return {"operation": "multiplication", "result": result}

# Endpoint for division
@app.post("/divide")
def divide_numbers(request: CalculationRequest):
    if request.number2 == 0:
        logging.warning("Division by zero attempted.")
        return {"operation": "division", "error": "Division by zero is not allowed"}
    result = request.number1 / request.number2
    logging.info(f"Division: {request.number1} / {request.number2} = {result}")
    add_to_history("division", result)
    return {"operation": "division", "result": result}

@app.post("/power")
def power_numbers(request: CalculationRequest):
    result = request.number1 ** request.number2
    logging.info(f"Power: {request.number1} ** {request.number2} = {result}")
    add_to_history("power", result)
    return {"operation": "power", "result": result}

@app.post("/sqrt")
def square_root(request: SingleNumberRequest):
    if request.number1 <0:
        logging.warning("Square root of negative number attempted.")
        return {"operation": "sqrt", "error": "Square root of negative number is not allowed"}
    result = math.sqrt(request.number1)
    logging.info(f"Square root: sqrt({request.number1}) = {result}")
    add_to_history("square_root", result)
    return {"operation": "square_root", "result": result}

# Endpoint to retrieve calculation history
@app.get("/history")
def get_history():
    return {"history": history}    