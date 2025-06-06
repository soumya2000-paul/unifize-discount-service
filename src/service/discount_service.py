from typing import List, Optional, Dict
from decimal import Decimal

from models.models import CartItem, CustomerProfile, PaymentInfo, DiscountedPrice, BrandTier

from .brand_discount import BrandDiscountCalculator
from .bank_discount import BankDiscountCalculator
from .category_discount import CategoryDiscountCalculator
from .voucher_discount import VoucherDiscountCalculator



class DiscountService:
    async def calculate_cart_discounts(
        self,
        cart_items: List[CartItem],
        customer: CustomerProfile,
        payment_info: Optional[PaymentInfo] = None,
        voucher_code: Optional[str] = None
    ) -> DiscountedPrice:
        original_price = Decimal("0")
        discounted_price = Decimal("0")
        applied_discounts: Dict[str, Decimal] = {}

        brand_discount = BrandDiscountCalculator()
        back_discount = BankDiscountCalculator()
        category_discount = CategoryDiscountCalculator()
        voucher_discount = VoucherDiscountCalculator()

        for item in cart_items:
            product = item.product
            price = product.base_price * item.quantity
            original_price += price

            brand_discount_percentage = brand_discount.get_discount(product)
            category_discount_percentage = category_discount.get_category_discount(product)

            price_after_brand = price * (1 - brand_discount_percentage)
            applied_discounts[f"Brand discount on {product.brand}"] = price - price_after_brand

            price_after_category = price_after_brand * (1 - category_discount_percentage)
            applied_discounts[f"Category discount on {product.category}"] = price_after_brand - price_after_category

            discounted_price += price_after_category
        
        bank_discount_percent = back_discount.get_bank_discount(payment_info)

        if bank_discount_percent:
            bank_discount = discounted_price * bank_discount_percent
            applied_discounts[f"{payment_info.bank_name} Bank Offer"] = bank_discount
            discounted_price -= bank_discount

        if voucher_code and voucher_discount.validate(voucher_code, cart_items):
            voucher_discount = voucher_discount.get_discount(voucher_code, discounted_price)
            applied_discounts[f"Voucher {voucher_code}"] = voucher_discount
            discounted_price -= voucher_discount

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
