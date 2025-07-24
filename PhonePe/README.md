# PhonePe Payment Gateway Stub

This folder contains a **backend stub for PhonePe payment integration** for the Dress Shopping App.  
It enables end-to-end integration testing and local dev without requiring real PhonePe credentials.

---

## Features

- `POST /phonepe/initiate` : Initiate a mock payment (returns a fake payment URL)
- `GET /phonepe/status/{payment_id}` : Check payment status (always returns SUCCESS for stubs)

**OpenAPI docs:** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Local Development

1. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

2. Run the server:

    ```
    uvicorn main:app --reload
    ```

---

## Integration

- The main backend/frontend can call these endpoints using HTTP.
- No real payment is performed. All data is mock/stubbed.
- To swap in a real PhonePe integration, replace the logic in `main.py` with actual API calls and secure credential management.

---

## Folder contents

- `main.py` - FastAPI stub server for mock PhonePe payment flow.
- `requirements.txt` - Required Python packages.
- `README.md` - This file.

---

## Security

- Never use this stub in production.
- Always validate and secure all payment handling in real integrations.

---
