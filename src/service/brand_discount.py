# src/calculation/brand_discount.py
from decimal import Decimal
from models.models import Product

class BrandDiscountCalculator:
    def get_discount(self, product: Product) -> Decimal:
        # for multiple brands, switch to switch-case than if-else
        if product.brand.lower() == "puma":
            if product.base_price >= Decimal("2000"):
                return Decimal("0.5")  # 50% discount
            return Decimal("0.4")  # Minimum 40%
        return Decimal("0")  # No discount for other brands