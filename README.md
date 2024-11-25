
# Calculation API

An enhanced API for performing basic and advanced math operations, built using FastAPI. It includes detailed logging, 
input validation, calculation history tracking with timestamps, and user authentication.

## Features
- **Input Validation**: Ensures correctness and prevents invalid values.
- **Error Handling**: Handles edge cases like division by zero or invalid inputs gracefully.
- **Calculation History with Timestamps**: Tracks and provides a history of all calculations performed during 
  the application's runtime, including the time each operation was performed (Format: `YYYY-MM-DD HH:MM:SS`).
- **User Authentication**: Protects endpoints by requiring a valid token for access.
- **Comprehensive API Documentation**: Available via FastAPI's Swagger UI.

## Endpoints

### User Authentication

#### Login
- **URL**: `/login`
- **Method**: POST
- **Description**: Authenticate users using form data (username and password) to obtain a token.
- **Request Example**:
  ```
  username=user
  password=pass
  ```
- **Response Example**:
  ```json
  {
      "message": "Login successful!",
      "token": "dummy-token"
  }
  ```

### Addition
- **URL**: `/add`
- **Method**: POST
- **Description**: Adds two numbers together.
- **Headers**:
  ```
  Authorization: dummy-token
  ```
- **Request Model**: `CalculationRequest` (includes `number1` and `number2` as floats).
- **Request Example**:
  ```json
  {
      "number1": 5,
      "number2": 3
  }
  ```
- **Response Example**:
  ```json
  {
      "operation": "addition",
      "result": 8,
      "timestamp": "2024-11-25 15:25:24"
  }
  ```

### Subtraction
- **URL**: `/subtract`
- **Method**: POST
- **Description**: Subtracts the second number from the first.
- **Headers**:
  ```
  Authorization: dummy-token
  ```
- **Request Example**:
  ```json
  {
      "number1": 10,
      "number2": 7
  }
  ```
- **Response Example**:
  ```json
  {
      "operation": "subtraction",
      "result": 3,
      "timestamp": "2024-11-25 15:25:36"
  }
  ```

### Multiplication
- **URL**: `/multiply`
- **Method**: POST
- **Description**: Multiplies two numbers together.
- **Headers**:
  ```
  Authorization: dummy-token
  ```
- **Request Example**:
  ```json
  {
      "number1": 4,
      "number2": 5
  }
  ```
- **Response Example**:
  ```json
  {
      "operation": "multiplication",
      "result": 20,
      "timestamp": "2024-11-25 15:25:38"
  }
  ```

### Division
- **URL**: `/divide`
- **Method**: POST
- **Description**: Divides the first number by the second. Raises an error if the divisor is zero.
- **Headers**:
  ```
  Authorization: dummy-token
  ```
- **Request Example**:
  ```json
  {
      "number1": 10,
      "number2": 2
  }
  ```
- **Response Example**:
  ```json
  {
      "operation": "division",
      "result": 5.0,
      "timestamp": "2024-11-25 15:25:40"
  }
  ```
- **Error Example** (Division by zero):
  ```json
  {
      "operation": "division",
      "error": "Division by zero is not allowed."
  }
  ```

### Power
- **URL**: `/power`
- **Method**: POST
- **Description**: Raises the first number to the power of the second.
- **Headers**:
  ```
  Authorization: dummy-token
  ```
- **Request Example**:
  ```json
  {
      "number1": 2,
      "number2": 3
  }
  ```
- **Response Example**:
  ```json
  {
      "operation": "power",
      "result": 8,
      "timestamp": "2024-11-25 15:25:42"
  }
  ```

### Square Root
- **URL**: `/sqrt`
- **Method**: POST
- **Description**: Calculates the square root of a single number. Only positive numbers are allowed.
- **Headers**:
  ```
  Authorization: dummy-token
  ```
- **Request Model**: `SingleNumberRequest` (includes `number1` as a positive float).
- **Request Example**:
  ```json
  {
      "number1": 16
  }
  ```
- **Response Example**:
  ```json
  {
      "operation": "square_root",
      "result": 4.0,
      "timestamp": "2024-11-25 15:25:44"
  }
  ```
- **Error Example** (Square root of a negative number):
  ```json
  {
      "operation": "square_root",
      "error": "Cannot calculate the square root of a negative number."
  }
  ```

### Calculation History
- **URL**: `/history`
- **Method**: GET
- **Description**: Retrieves the calculation history along with timestamps.
- **Headers**:
  ```
  Authorization: dummy-token
  ```
- **Response Example**:
  ```json
  {
      "history": [
          {"operation": "addition", "result": 8, "timestamp": "2024-11-25 15:25:24"},
          {"operation": "division", "result": 5.0, "timestamp": "2024-11-25 15:25:40"}
      ]
  }
  ```

## Setup

### Install Dependencies Using requirements.txt
Run the following command to install all required dependencies:
```bash
pip install -r requirements.txt
```
Make sure that the `requirements.txt` file is located in the root directory of the project.

### Run the Application
Use the following command to start the FastAPI application:
```bash
uvicorn main:app --reload
```

### Open the API Documentation
After running the application, open your browser and visit:
```text
http://127.0.0.1:8000/docs
```

## Dependencies
- `fastapi`: Web framework for building APIs.
- `uvicorn`: ASGI server for running the FastAPI app.
- `pydantic`: For data validation and settings management.
- `math`: Python's standard library for mathematical operations.
- `logging`: Python's standard library for logging and debugging.
- `python-multipart`: Required for handling form data.

## Future Improvements
- Expand API to include advanced mathematical functions like trigonometry.
- Implement database integration for persistent storage of history.
- Add role-based user permissions for enhanced security.
