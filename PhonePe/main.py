from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

# PhonePe Payment API stub using FastAPI

app = FastAPI(
    title="PhonePe Payment API Stub",
    description="Stub API for PhonePe payment integration with the Dress Shopping App. This is for development and modular integration testing purposes only.",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "payments",
            "description": "API for initiating and verifying PhonePe payments."
        }
    ]
)

# Payment initiation request model
class PaymentRequest(BaseModel):
    # PUBLIC_INTERFACE
    user_id: str = Field(..., description="Unique identifier of the paying user")
    order_id: str = Field(..., description="Unique identifier for the placed order")
    amount: float = Field(..., description="The amount (in INR) to be paid")
    phone: str = Field(..., description="Phone number of the user")
    # Add any other meta as needed for mock

# Payment initiation response model
class PaymentInitResponse(BaseModel):
    # PUBLIC_INTERFACE
    payment_id: str = Field(..., description="Unique transaction/payment ID")
    status: str = Field(..., description="Status of the payment request (e.g. PENDING)")
    payment_url: str = Field(..., description="Mock URL simulating PhonePe payment page")

# Payment status response model
class PaymentStatusResponse(BaseModel):
    # PUBLIC_INTERFACE
    payment_id: str = Field(..., description="Unique transaction/payment ID")
    order_id: str = Field(..., description="Order ID associated with this payment")
    status: str = Field(..., description="Payment status ('SUCCESS','FAILED','PENDING')")
    amount: float = Field(..., description="Amount paid/attempted")
    phone: str = Field(..., description="Phone number used for payment")


# Public API endpoints

# PUBLIC_INTERFACE
@app.post("/phonepe/initiate", response_model=PaymentInitResponse, tags=["payments"], summary="Initiate PhonePe Payment", description="Initiates a PhonePe payment operation and returns a simulated payment link.")
def initiate_payment(req: PaymentRequest):
    """
    Initiate a PhonePe mock payment. Returns a mock payment_id and payment URL.
    Parameters:
        - user_id: str
        - order_id: str
        - amount: float
        - phone: str
    Returns:
        - payment_id: str
        - status: str ('PENDING')
        - payment_url: str
    """
    # In real integration, call PhonePe API, generate payment request, store transaction etc.
    payment_id = f"mock_phonepe_{req.order_id}"
    payment_url = f"https://mock.phonepe.com/pay/{payment_id}"
    return PaymentInitResponse(
        payment_id=payment_id,
        status="PENDING",
        payment_url=payment_url
    )

# PUBLIC_INTERFACE
@app.get("/phonepe/status/{payment_id}", response_model=PaymentStatusResponse, tags=["payments"], summary="Check PhonePe Payment Status", description="Check the status of a PhonePe payment by transaction ID.")
def check_payment_status(payment_id: str, order_id: Optional[str] = None):
    """
    Check mock payment status of a PhonePe transaction. Always returns mock data for stubbing.
    Parameters:
        - payment_id: str
        - order_id: Optional[str]
    Returns:
        - payment_id: str
        - order_id: str
        - status: str ('SUCCESS'/'FAILED'/'PENDING')
        - amount: float
        - phone: str
    """
    # For stub, all payments succeed if payment_id starts with known prefix.
    if payment_id.startswith("mock_phonepe_"):
        return PaymentStatusResponse(
            payment_id=payment_id,
            order_id=order_id or payment_id.replace("mock_phonepe_", ""),
            status="SUCCESS",
            amount=1000.0,  # Mock amount
            phone="9999999999"
        )
    else:
        raise HTTPException(status_code=404, detail="Payment ID not found")

# PUBLIC_INTERFACE
@app.get("/", tags=["payments"], summary="PhonePe API Landing", description="Landing endpoint for PhonePe stub API.")
def root():
    """Root endpoint - PhonePe Payment API stub running."""
    return {"msg": "PhonePe Payment API Stub running"}

