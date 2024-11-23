
# Calculation API

An enhanced API for performing basic and advanced math operations, built using FastAPI. It includes detailed logging, input validation, and calculation history tracking.

## Features
- **Input Validation**: Ensures correctness and prevents invalid values.
- **Error Handling**: Handles edge cases like division by zero or invalid inputs gracefully.
- **Calculation History**: Tracks and provides a history of all calculations performed during the application's runtime.
- **Comprehensive API Documentation**: Available via FastAPI's Swagger UI.

## Endpoints

### Addition
- **URL**: `/add`
- **Method**: POST
- **Description**: Add two numbers.
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
      "result": 8
  }
  ```

### Subtraction
- **URL**: `/subtract`
- **Method**: POST
- **Description**: Subtract two numbers.
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
      "result": 3
  }
  ```

### Multiplication
- **URL**: `/multiply`
- **Method**: POST
- **Description**: Multiply two numbers.
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
      "result": 20
  }
  ```

### Division
- **URL**: `/divide`
- **Method**: POST
- **Description**: Divide two numbers.
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
      "result": 5.0
  }
  ```
- **Error Example** (Division by zero):
  ```json
  {
      "operation": "division",
      "error": "Division by zero is not allowed"
  }
  ```

### Power
- **URL**: `/power`
- **Method**: POST
- **Description**: Raise `number1` to the power of `number2`.
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
      "result": 8
  }
  ```

### Square Root
- **URL**: `/sqrt`
- **Method**: POST
- **Description**: Compute the square root of a single number (`number1`).
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
      "result": 4.0
  }
  ```
- **Error Example** (Square root of a negative number):
  ```json
  {
      "operation": "square_root",
      "error": "Square root of negative number is not allowed"
  }
  ```

### Calculation History
- **URL**: `/history`
- **Method**: GET
- **Description**: Retrieve a history of all calculations performed during the application's runtime.
- **Response Example**:
  ```json
  {
      "history": [
          {"operation": "addition", "result": 8},
          {"operation": "division", "result": 5.0}
      ]
  }
  ```

## Setup

### Install Dependencies
Run the following command to install the required dependencies:
```bash
pip install -r requirements.txt
```

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

## Future Improvements
- Add user authentication for personalized history tracking.
- Expand API to include advanced mathematical functions like trigonometry.
- Implement database integration for persistent storage of history.