# Calculation API

An enhanced API for performing basic and advanced math operations, built using FastAPI. 
It includes detailed logging, input validation, calculation history tracking with timestamps, 
and user authentication.

## Features

- **Input Validation**: Ensures correctness and prevents invalid values.
- **Error Handling**: Handles edge cases like division by zero or invalid inputs gracefully.
- **Calculation History with Timestamps**: Tracks and provides a history of all calculations performed 
  during the application's runtime, including the time each operation was performed (Format: `YYYY-MM-DD HH:MM:SS`).
- **User Authentication**: Protects endpoints by requiring a valid token for access.
- **Comprehensive API Documentation**: Available via FastAPI's Swagger UI.

## Endpoints

### User Authentication

#### Login
- **URL**: `/login`
- **Method**: POST
- **Description**: Authenticate users using form data (username and password) to obtain a token.

- **Request Example**:
  ```json
  {
    "username": "user",
    "password": "pass"
  }

   ```

- **Response Example**:
  ```json
  {
    "access_token": "dummy-token",
    "token_type": "bearer"
  }

  ```

- **Authorization**: The token received here should be included in the `Authorization` header of subsequent requests.

---

### Basic Operations

#### Addition
- **URL**: `/add`
- **Method**: POST
- **Description**: Adds two numbers together.
- **Headers**:
  ```text
  Authorization: Bearer dummy-token
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
    "timestamp": "2024-11-27 21:00:00"
  }

  ```

#### Subtraction
- **URL**: `/subtract`
- **Method**: POST
- **Description**: Subtracts the second number from the first.
- **Headers**:
  ```text
  Authorization: Bearer dummy-token
  ```
- **Request Model**: `CalculationRequest` (includes `number1` and `number2` as floats).
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
    "timestamp": "2024-11-27 21:10:00"
  }

  ```

#### Multiplication
- **URL**: `/multiply`
- **Method**: POST
- **Description**: Multiplies two numbers together.
- **Headers**:
  ```text
  Authorization: Bearer dummy-token
  ```
- **Request Model**: `CalculationRequest` (includes `number1` and `number2` as floats).
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
      "operation": "multiplication",
      "result": 20,
      "timestamp": "2024-11-27 21:20:00"
  }
  ```

#### Division
- **URL**: `/divide`
- **Method**: POST
- **Description**: Divides the first number by the second. Raises an error if the divisor is zero.
- **Headers**:
  ```text
  Authorization: Bearer dummy-token
  ```
- **Request Model**: `CalculationRequest` (includes `number1` and `number2` as floats).
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
    "result": 5,
    "timestamp": "2024-11-27 21:30:00"
  }

  ```
- **Error Example** (Division by zero):
  ```json
  {
    "operation": "division",
    "result": "error",
    "timestamp": "2024-11-27 21:30:00",
    "error_message": "Division by zero is not allowed."
  }
  ```
  ```text
  HTTP Status Code: 400 Bad Request
  ```

#### Power
- **URL**: `/power`
- **Method**: POST
- **Description**: Raises the first number to the power of the second.
- **Headers**:
  ```text
  Authorization: Bearer dummy-token
  ```
- **Request Model**: `CalculationRequest` (includes `number1` and `number2` as floats).
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
    "timestamp": "2024-11-27 21:40:00"
  }
  ```

#### Square Root
- **URL**: `/sqrt`
- **Method**: POST
- **Description**: Calculates the square root of a single number. Only positive numbers are allowed.
- **Headers**:
  ```text
  Authorization: Bearer dummy-token
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
    "result": 4,
    "timestamp": "2024-11-27 21:50:00"
  }
  ```
- **Error Example** (Square root of a negative number):
  ```json
  {
    "operation": "square_root",
    "result": "error",
    "timestamp": "2024-11-27 21:50:00",
    "error_message": "Cannot calculate the square root of a negative number."
  }
  ```
  ```text
  HTTP Status Code: 400 Bad Request
  ```

#### Calculation History
- **URL**: `/history`
- **Method**: GET
- **Description**: Retrieves the calculation history along with timestamps.

- **Headers**:
  ```text
  Authorization: Bearer dummy-token
  ```
- **Response Example**:
  ```json
  {
    "history": [
        {"operation": "addition", "result": 8, "timestamp": "2024-11-27 21:00:00"},
        {"operation": "subtraction", "result": 3, "timestamp": "2024-11-27 21:10:00"}
    ]
  }
  ```

---

## Setup

### Install Dependencies Using requirements.txt
Create a `requirements.txt` file in the project root. This file lists all the necessary Python packages for the project. You can install them all at once with:
```bash
pip install -r requirements.txt 
```
These are the basic dependencies needed to run the FastAPI application.

- `fastapi`: The web framework to build the API.
- `uvicorn`: The ASGI server for running the FastAPI app.
- `pydantic`: Used for data validation and settings management.
- `math`: Python's standard library for mathematical operations.
- `logging`: Python's standard library for logging and debugging.
- `python-multipart`: Required for handling form data.
- `python-dotenv`: For loading environment variables from a `.env` file.

### Run the Application
Once the dependencies are installed, start the FastAPI application by running the following command:
```bash
uvicorn main:app --reload
```

### Access the Documentation
After running the application, open your browser and visit the following URL to access the Swagger UI and interact with the API:
```text
http://127.0.0.1:8000/docs
```

### Setting up `.env` file
To run the project locally, you need to create a `.env` file for storing sensitive configuration values. Follow these steps:

1.  **Create a `.env` file**: Create a file named `.env` in the root directory of your project.
2. **Add the following lines to the `.env` file**:
   ```text
   SECRET_KEY=your-secret-key
   LOG_LEVEL=INFO
   ```
3. **Replace `your-secret-key`**: Replace it with any secret value you prefer. This key is essential for token generation and authentication.
4. **Save the file**. Save the file in the root directory of your project.
5. **Ensure `.env` is ignored by Git**: Verify that `.env` is already listed in the `.gitignore` file to prevent it from being uploaded to version control.

---

## Token Management and Security
Proper management of authentication tokens is essential to maintain application security. Here are the key points:

1. **Environment Variables**:
   Use a `.env` file to store sensitive values like `SECRET_KEY` and `LOG_LEVEL`. Refer to the "Setting up `.env` file" section for details.

2. **Short Expiry Times**:
   Set short expiry times for tokens (e.g., 15 minutes to 1 hour) to minimize risks if a token is compromised.

3. **Token Encryption**:
   If tokens are stored persistently (e.g., in a database), use encryption with libraries like `cryptography`.

4. **Logs**:
   Ensure logs do not expose sensitive data such as tokens or passwords. Adjust logging levels appropriately using `LOG_LEVEL` in the `.env` file.

5. **Optional Refresh Tokens**:
   For production environments, consider using refresh tokens to issue new access tokens when the original expires.


### Token Expiry and Refresh Tokens
- **Short Expiry Time**: Set a short expiration time for tokens. This reduces the risk if a token is compromised. Consider using **refresh tokens** for long-term sessions.
- You can implement refresh tokens to provide a new access token after the old one expires, which enhances security while maintaining user convenience.

### Refresh Tokens (Optional)
- **Refresh Token**: In production environments, instead of storing long-lived access tokens, use short-lived access tokens paired with refresh tokens. When the access token expires, the user can send the refresh token to obtain a new access token.
- This improves security because the access token has a short lifespan, but the refresh token is stored securely and can only be used for token renewal.

### Encrypt Tokens
- Tokens stored in the database should be encrypted to prevent unauthorized access. You can use libraries like `cryptography` or `PyCryptodome` to encrypt tokens before storing them.
- Always use strong encryption algorithms and store the encryption keys in a secure manner (e.g., environment variables).

### Securely Store Sensitive Data in Environment Variables
- Store all sensitive keys (e.g., `SECRET_KEY`, `ACCESS_TOKEN_SECRET`) in environment variables rather than hardcoding them into your code. 
- Use a `.env` file and libraries like `python-dotenv` to load these variables securely.
- Ensure that `.env` files are never committed to version control (e.g., Git). Add `.env` to `.gitignore`.

---

## Future Improvements
- Expand API to include advanced mathematical functions like trigonometry.
- Implement database integration for persistent storage of history.
- Add role-based user permissions for enhanced security.
- Expand test coverage for additional edge cases (e.g., invalid token formats, extreme numerical inputs).