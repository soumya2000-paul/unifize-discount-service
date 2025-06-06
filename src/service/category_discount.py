from decimal import Decimal
from models.models import Product

class CategoryDiscountCalculator:
    """
    A class to calculate category-specific discounts.
    """

    def get_category_discount(self, product: Product) -> Decimal:
        if product.category.lower() == "t-shirts":
            return Decimal("0.1")
        return Decimal("0")
