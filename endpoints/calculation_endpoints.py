from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from models.calcultations.amortization import calculate_monthly_payment, generate_amortization_schedule
from models.database_models.loan_details import LoanDetails, AmortizationSchedule

router = APIRouter()

@router.post("/amortization", response_model=AmortizationSchedule)
def get_amortization_schedule(loan_details: LoanDetails):
    try:
        principal = loan_details.principal
        annual_interest_rate = loan_details.annual_interest_rate
        years = loan_details.years
        property_tax = loan_details.property_tax
        extra_monthly_payment = loan_details.extra_monthly_payment
        extra_yearly_payment = loan_details.extra_yearly_payment
        extra_one_time_payments = loan_details.extra_one_time_payments
        extra_one_time_amount = loan_details.extra_one_time_amount
        
        monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years, property_tax, extra_monthly_payment)
        schedule = generate_amortization_schedule(principal, annual_interest_rate, years, property_tax, extra_monthly_payment, extra_yearly_payment, extra_one_time_payments, extra_one_time_amount)
        
        return {
            "monthly_payment": round(monthly_payment, 2),
            "schedule": schedule
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")