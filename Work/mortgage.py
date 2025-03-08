# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    principal_with_interest = principal * (1+rate/12)
    # prevent possible overpaying
    if payment > principal_with_interest:
        payment = principal_with_interest
        extra_payment = 0

    # extra payment the first 12 months
    total_payment = payment
    if extra_payment_start_month <= months <= extra_payment_end_month:
        # prevent possible overpaying
        if payment + extra_payment > principal_with_interest:
            extra_payment = principal_with_interest - payment
        total_payment += extra_payment

    months += 1
    principal = principal_with_interest - total_payment
    total_paid = total_paid + total_payment
    print(months, total_paid, principal)

#print('Total paid:', total_paid)
print(f'Total paid: {total_paid}')
#print('Number of months:', months)
print(f'Number of months: {months}')