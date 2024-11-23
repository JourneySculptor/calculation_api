
# Calculation API

A simple API for basic math operations built with FastAPI.

## Endpoints

### Addition
- **URL**: `/add`
- **Method**: POST
- **Description**: Add two numbers.
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
      "number1": 5,
      "number2": 3
  }
  ```
- **Response Example**:
  ```json
  {
      "operation": "subtraction",
      "result": 2
  }
  ```

### Multiplication
- **URL**: `/multiply`
- **Method**: POST
- **Description**: Multiply two numbers.
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
      "operation": "multiplication",
      "result": 15
  }
  ```

### Division
- **URL**: `/divide`
- **Method**: POST
- **Description**: Divide two numbers.
- **Request Example**:
  ```json
  {
      "number1": 6,
      "number2": 3
  }
  ```
- **Response Example**:
  ```json
  {
      "operation": "division",
      "result": 2.0
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
- **Description**: Raise number1 to the power of number2.
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
- **Description**: Compute the square root of number1.
- **Request Example**:
  ```json
  {
      "number1": 9
  }
  ```
- **Response Example**:
  ```json
  {
      "operation": "square_root",
      "result": 3.0
  }
  ```

- **Error Example** (Square root of a negative number):
  ```json
  {
      "operation": "sqrt",
      "error": "Square root of negative number is not allowed"
  }
  ```

### Calculation History
- **URL**: `/history`
- **Method**: GET
- **Description**: Retrieve the history of all calculations.
- **Response Example**:
  ```json
  {
      "history": [
          {"operation": "addition", "result": 8},
          {"operation": "subtraction", "result": 2}
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
This project uses the following Python packages:
- `fastapi`
- `uvicorn`
- `pydantic`