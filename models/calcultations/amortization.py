# amortization_calculator.py
from datetime import date

def calculate_monthly_payment(principal, annual_interest_rate, years, property_tax, extra_monthly_payment=0):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    num_payments = years * 12
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)
    monthly_payment_with_tax_and_extra = monthly_payment + property_tax / 12 + extra_monthly_payment  # Include monthly property tax and extra monthly payment
    return monthly_payment_with_tax_and_extra

def generate_amortization_schedule(principal, annual_interest_rate, years, property_tax, extra_monthly_payment=0, extra_yearly_payment=0, extra_one_time_payments=None, extra_one_time_amount=0):
    if extra_one_time_payments is None:
        extra_one_time_payments = []

    monthly_payment_with_tax_and_extra = calculate_monthly_payment(principal, annual_interest_rate, years, property_tax, extra_monthly_payment)
    monthly_interest_rate = annual_interest_rate / 12 / 100
    num_payments = years * 12
    schedule = []

    remaining_balance = principal
    current_date = date.today()

    for i in range(1, num_payments + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = (monthly_payment_with_tax_and_extra - property_tax / 12 - extra_monthly_payment) - interest_payment
        remaining_balance -= principal_payment

        extra_payment = extra_monthly_payment

        # Apply yearly extra payment
        if i % 12 == 0:
            extra_payment += extra_yearly_payment
            remaining_balance -= extra_yearly_payment

        # Apply one-time extra payments
        if current_date in extra_one_time_payments:
            extra_payment += extra_one_time_amount
            remaining_balance -= extra_one_time_amount

        remaining_balance -= extra_payment

        schedule.append({
            "Payment_Number": i,
            "Monthly_Payment": round(monthly_payment_with_tax_and_extra, 2),
            "Principal_Payment": round(principal_payment, 2),
            "Interest_Payment": round(interest_payment, 2),
            "Property_Tax": round(property_tax / 12, 2),
            "Extra_Payment": round(extra_payment, 2),
            "Remaining_Balance": round(remaining_balance, 2)
        })

        current_date = current_date.replace(month=(current_date.month % 12) + 1)
        if current_date.month == 1:
            current_date = current_date.replace(year=current_date.year + 1)

    return schedule