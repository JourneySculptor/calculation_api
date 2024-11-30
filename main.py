from fastapi import FastAPI, Form, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.openapi.utils import get_openapi
import jwt
from datetime import datetime, timedelta, timezone
from pydantic import BaseModel, Field
import math
import logging
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Configure logging for debugging
log_level = os.getenv("LOG_LEVEL", "INFO").upper() # Default to INFO
logging.basicConfig(level=log_level)

# Secret key and algorithm for JWT
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# OAuth2PasswordBearer instance to get the token from the request
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)

# Request body models for validation using Pydantic
class CalculationRequest(BaseModel):
    number1: float = Field(..., description="First number for calculation")
    number2: float = Field(..., description="Second number for calculation")

class SingleNumberRequest(BaseModel):
    number1: float = Field(..., description="The number to perform the operation on")

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Calculation App API",
        version="1.0.0",
        description="API for calculations with authentication",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
        }
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Function to create JWT access token
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta  # Use timezone-aware datetime
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)  # Default expiration is 15 minutes
    to_encode.update({"exp": expire})  # Add expiration time to the token data
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  # Encode the data into a JWT
    return encoded_jwt

@app.post("/login", description="Authenticates the user and provides a JWT token for accessing secured endpoints.")
def login(username: str = Form(...), password: str = Form(...)):
    if username == "user" and password == "pass":  # Dummy check (replace with DB validation)
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"sub": username}, expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid username or password")

# Function to verify authentication token
def verify_token(token: str = Depends(oauth2_scheme)):  # Use oauth2_scheme to get token from header
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # Decode token
        username: str = payload.get("sub")  # Extract username from the token
        if username is None:
            raise credentials_exception
        return username
    except jwt.PyJWTError:
        raise credentials_exception

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

@app.get("/history", description="Retrieves the calculation history.")
def get_history(token: str = Depends(verify_token)):
    return {"history": history}
