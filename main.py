from fastapi import FastAPI, Form, HTTPException, Depends
from fastapi.openapi.utils import get_openapi
from fastapi.security import APIKeyHeader
from pydantic import BaseModel, Field
from datetime import datetime
import math
import logging

# Initialize FastAPI app
app = FastAPI()

# Configure logging for debugging
logging.basicConfig(level=logging.INFO)

# Security scheme for Swagger UI
api_key_header = APIKeyHeader(name="Authorization", auto_error=True)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Calculation API",
        version="1.0.0",
        description="An API for basic math operations with authentication",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "APIKeyHeader": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
        }
    }
    openapi_schema["security"] = [{"APIKeyHeader": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Request models
class CalculationRequest(BaseModel):
    number1: float = Field(gt=-1e6, lt=1e6, description="Value must be between -1,000,000 and 1,000,000")
    number2: float = Field(gt=-1e6, lt=1e6, description="Value must be between -1,000,000 and 1,000,000")

class SingleNumberRequest(BaseModel):
    number1: float = Field(gt=0, lt=1e6, description="Value must be between 0 and 1,000,000")

# Dummy authentication credentials
valid_username = "user"
valid_password = "pass"

@app.post("/login", description="Authenticates the user and provides a dummy token for accessing secured endpoints.")
def login(username: str = Form(...), password: str = Form(...)):
    if username == valid_username and password == valid_password:
        return {"message": "Login successful!", "token": "dummy-token"}
    raise HTTPException(status_code=401, detail="Invalid username or password")

# Function to verify authentication token
def verify_token(token: str = Depends(api_key_header)):
    if token != "dummy-token":
        raise HTTPException(status_code=403, detail="Invalid or missing token")

# Initialize history list
history = []

# Add calculation to history
def add_to_history(operation: str, result: float):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append({"operation": operation, "result": result, "timestamp": timestamp})

# Unified function for calculations and logging
def calculate_and_log(operation: str, func, *args):
    try:
        result = func(*args)
        add_to_history(operation, result)
        return {"operation": operation, "result": result, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
    except Exception as e:
        logging.error(f"Error during {operation}: {e}")
        raise HTTPException(status_code=500, detail="An internal error occurred.")

# Endpoints for math operations
@app.post("/add", description="Adds two numbers together.")
def add_numbers(request: CalculationRequest, token: str = Depends(verify_token)):
    return calculate_and_log("addition", lambda x, y: x + y, request.number1, request.number2)

@app.post("/subtract", description="Subtracts the second number from the first.")
def subtract_numbers(request: CalculationRequest, token: str = Depends(verify_token)):
    return calculate_and_log("subtraction", lambda x, y: x - y, request.number1, request.number2)

@app.post("/multiply", description="Multiplies two numbers together.")
def multiply_numbers(request: CalculationRequest, token: str = Depends(verify_token)):
    return calculate_and_log("multiplication", lambda x, y: x * y, request.number1, request.number2)

@app.post("/divide", description="Divides the first number by the second.")
def divide_numbers(request: CalculationRequest, token: str = Depends(verify_token)):
    if request.number2 == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
    return calculate_and_log("division", lambda x, y: x / y, request.number1, request.number2)

@app.post("/power", description="Raises the first number to the power of the second.")
def power_numbers(request: CalculationRequest, token: str = Depends(verify_token)):
    return calculate_and_log("power", lambda x, y: x ** y, request.number1, request.number2)

@app.post("/sqrt", description="Calculates the square root of a single number.")
def square_root(request: SingleNumberRequest, token: str = Depends(verify_token)):
    return calculate_and_log("square_root", math.sqrt, request.number1)

# Endpoint to retrieve calculation history
@app.get("/history", description="Retrieves the calculation history.")
def get_history(token: str = Depends(verify_token)):
    return {"history": history}
