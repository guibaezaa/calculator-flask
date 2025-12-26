# Calculator Flask

A small Flask-based API that exposes four calculator endpoints. Each endpoint runs a different calculation strategy; some use NumPy for statistical operations.

## Features
- Four calculator endpoints (POST): `/calculator/1`, `/calculator/2`, `/calculator/3`, `/calculator/4`
- Input validation and error handling
- Pluggable driver for numeric operations (NumPy)

## Project structure

- `run.py` — application entry point
- `src/main/server/server.py` — Flask app and blueprint registration
- `src/main/routes/calculators.py` — API routes for calculators
- `src/main/factories/*_factory.py` — factories that assemble calculators and their drivers
- `src/calculators/` — implementations of the four calculators
- `src/drivers/numpy_handler.py` — NumPy-based driver for statistics

## Requirements
- Python 3.8+
- Flask
- NumPy

You can install dependencies with pip:

```bash
python -m pip install flask numpy
```

## Run locally

Start the app with:

```bash
python run.py
```

The server listens by default on `http://0.0.0.0:3000`.

## API Usage

All endpoints accept `application/json` POST requests.

- Calculator 1
	- Endpoint: `POST /calculator/1`
	- Body: `{ "number": 9.5 }`
	- Example response:
		```json
		{ "data": { "Calculator": 1, "result": 12.34 } }
		```

- Calculator 2
	- Endpoint: `POST /calculator/2`
	- Body: `{ "numbers": [1, 2, 3, 4] }`
	- Example response:
		```json
		{ "data": { "Calculator": 2, "result": 0.42 } }
		```

- Calculator 3
	- Endpoint: `POST /calculator/3`
	- Body: `{ "numbers": [1, 2, 3] }`
	- Example response:
		```json
		{ "data": { "Calculator": 3, "variance": 0.67, "Success": true } }
		```

- Calculator 4
	- Endpoint: `POST /calculator/4`
	- Body: `{ "numbers": [1, 2, 3] }`
	- Example response:
		```json
		{ "data": { "Calculator": 4, "result": 2.00 } }
		```

## Error handling

- Missing or invalid JSON fields return `400` with an error message.
- Unexpected errors return `500` with a generic message.

## Tests

There are simple unit tests under `src/calculators/` (files ending with `_test.py`). Run them with your preferred test runner (for example, `pytest`).

## Notes

- The numeric driver uses NumPy (`src/drivers/numpy_handler.py`). You can replace this driver with another implementation by following the `DriverHandlerInterface`.
