# Import necessary modules
from fastapi import FastAPI, Form, HTTPException, Depends, Header
from fastapi.security import APIKeyHeader 
from pydantic import BaseModel, Field
import logging
import math

# Initialize FastAPI app
app = FastAPI()

# Configure logging for debugging
logging.basicConfig(level=logging.INFO)

# Define request model for input validation
class CalculationRequest(BaseModel):
    number1: float = Field(gt=-1e6, lt=1e6, description="Value must be between -1,000,000 and 1,000,000")
    number2: float = Field(gt=-1e6, lt=1e6, description="Value must be between -1,000,000 and 1,000,000")

# Define request model for operations requiring a single number
class SingleNumberRequest(BaseModel):
    number1: float = Field(gt=0, lt=1e6, description="Value must be between 0 and 1,000,000")

# Initialize history list
history = []

# Add calculation to history
def add_to_history(operation: str, result: float):
    history.append({"operation": operation, "result": result})

# Unified function for calculations and logging
def calculate_and_log(operation: str, func, *args):
    try:
        result = func(*args)
        logging.info(f"{operation.capitalize()}: {args} = {result}")
        add_to_history(operation, result)
        return {"operation": operation, "result": result}
    except Exception as e:
        logging.error(f"Error during {operation}: {e}")
        return {"operation": operation, "error": str(e)}

# Dummy credentials for authentication
valid_username = "user"
valid_password = "pass"

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    if username == valid_username and password == valid_password:
        return {"message": "Login successful!", "token": "dummy-token"}
    raise HTTPException(status_code=401, detail="Invalid username or password")

# Security scheme for token verification
api_key_header = APIKeyHeader(name="Authorization")

# Function to verify authentication token
def verify_token(token: str = Depends(api_key_header)):
    if token != "dummy-token":
        raise HTTPException(status_code=403, detail="Invalid or missing token")

# Endpoint for addition
@app.post("/add")
def add_numbers(request: CalculationRequest, token: str = Depends(verify_token)):
    return calculate_and_log("addition", lambda x, y: x +y, request.number1, request.number2 )

# Endpoint for subtraction
@app.post("/subtract")
def subtract_numbers(request: CalculationRequest, token: str = Depends(verify_token)):
    result = request.number1 - request.number2
    return calculate_and_log("subtraction", lambda x, y: x - y, request.number1, request.number2)

# Endpoint for multiplication
@app.post("/multiply")
def multiply_numbers(request: CalculationRequest, token: str = Depends(verify_token)):
    return calculate_and_log("multiplication", lambda x, y: x * y, request.number1, request.number2)

# Endpoint for division
@app.post("/divide")
def divide_numbers(request: CalculationRequest, token: str = Depends(verify_token)):
    if request.number2 == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
    return calculate_and_log("division", lambda x, y: x / y, request.number1, request.number2)


@app.post("/power")
def power_numbers(request: CalculationRequest, token: str = Depends(verify_token)):
    return calculate_and_log("power", lambda x, y: x ** y, request.number1, request.number2)

@app.post("/sqrt")
def square_root(request: SingleNumberRequest, token: str = Depends(verify_token)):
    if request.number1 < 0:
        raise HTTPException(status_code=400, detail="Cannot calculate the square root of a negative number.")
    return calculate_and_log("square_root", math.sqrt, request.number1)


# Endpoint to retrieve calculation history
@app.get("/history")
def get_history(token: str = Depends(verify_token)):
    return {"history": history}
