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

### Error Responses
- **Error Example**:
  ```json
  {
      "detail": [
          {
              "loc": ["body", "number1"],
              "msg": "field required",
              "type": "value_error.missing"
          }
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
