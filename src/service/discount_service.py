from typing import List, Optional, Dict
from decimal import Decimal
from models.models import CartItem, CustomerProfile, PaymentInfo, DiscountedPrice, BrandTier

class DiscountService:
    async def calculate_cart_discounts(
        self,
        cart_items: List[CartItem],
        customer: CustomerProfile,
        payment_info: Optional[PaymentInfo] = None
    ) -> DiscountedPrice:
        original_price = Decimal("0")
        discounted_price = Decimal("0")
        applied_discounts: Dict[str, Decimal] = {}

        for item in cart_items:
            product = item.product
            price = product.base_price * item.quantity
            original_price += price

            brand_discount = Decimal("0.4") if product.brand.lower() == "puma" else Decimal("0")
            category_discount = Decimal("0.1") if product.category.lower() == "t-shirts" else Decimal("0")

            price_after_brand = price * (1 - brand_discount)
            applied_discounts[f"Brand discount on {product.brand}"] = price - price_after_brand

            price_after_category = price_after_brand * (1 - category_discount)
            applied_discounts[f"Category discount on {product.category}"] = price_after_brand - price_after_category

            discounted_price += price_after_category

        if payment_info and payment_info.bank_name == "ICICI":
            bank_discount = discounted_price * Decimal("0.1")
            applied_discounts["ICICI Bank Offer"] = bank_discount
            discounted_price -= bank_discount

        return DiscountedPrice(
            original_price=original_price,
            final_price=discounted_price,
            applied_discounts=applied_discounts,
            message="All applicable discounts have been applied"
        )

    async def validate_discount_code(
        self,
        code: str,
        cart_items: List[CartItem],
        customer: CustomerProfile
    ) -> bool:
        if code != "SUPER69":
            return False

        for item in cart_items:
            if item.product.brand_tier == BrandTier.PREMIUM:
                return False

        return True
