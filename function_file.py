def calculate_offer1(amt,off_pct,shipping_charges):
    offer_applied_amt = amt - (amt * off_pct)
    total_bill_amt = offer_applied_amt + shipping_charges
    return total_bill_amt


