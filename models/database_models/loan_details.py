from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class LoanDetails(BaseModel):
    principal: float
    annual_interest_rate: float
    years: int
    property_tax: float
    extra_monthly_payment: Optional[float] = 0  # Add extra monthly payment
    extra_yearly_payment: Optional[float] = 0  # Add extra yearly payment
    extra_one_time_payments: Optional[List[date]] = []  # Add extra one-time payments with specific dates
    extra_one_time_amount: Optional[float] = 0  # Add extra one-time payment amount

class PaymentDetail(BaseModel):
    Payment_Number: int
    Monthly_Payment: float
    Principal_Payment: float
    Interest_Payment: float
    Property_Tax: float
    Extra_Payment: float
    Remaining_Balance: float

class AmortizationSchedule(BaseModel):
    monthly_payment: float
    schedule: List[PaymentDetail]