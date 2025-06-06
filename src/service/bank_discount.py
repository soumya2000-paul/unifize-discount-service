from decimal import Decimal
from typing import Optional
from models.models import PaymentInfo
class BankDiscountCalculator:
    """
    A class to calculate bank-specific discounts.
    """
    
    def get_bank_discount(self, payment_info: Optional[PaymentInfo]) -> Decimal:
        if payment_info and payment_info.bank_name == "ICICI":
            return Decimal("0.1")
        return Decimal("0")
