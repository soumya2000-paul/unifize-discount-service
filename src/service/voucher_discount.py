from decimal import Decimal
from typing import List
from models.models import CartItem, CustomerProfile, BrandTier
from data.fake_data import valid_voucher

class VoucherDiscountCalculator:
    def validate(self, code: str, cart_items: List[CartItem]) -> bool:
        if code not in valid_voucher:
            return False

        for item in cart_items:
            if item.product.brand_tier == BrandTier.PREMIUM:
                return False

        return True

    def get_discount(self, code: str, total_after_all_discounts: Decimal) -> Decimal:
        match code:
            case "SUPER69":
                return total_after_all_discounts * Decimal("0.69")
            case "SAVE20":
                return total_after_all_discounts * Decimal("0.20")
            case _:
                return Decimal("0")