from dataclasses import dataclass
from typing import List, Optional, Dict
from decimal import Decimal
from enum import Enum

class BrandTier(Enum):
    PREMIUM = "premium"
    REGULAR = "regular"
    BUDGET = "budget"

@dataclass
class Product:
    id: str
    brand: str
    brand_tier: BrandTier
    category: str
    base_price: Decimal
    current_price: Decimal  # After brand/category discount

@dataclass
class CartItem:
    product: Product
    quantity: int
    size: str

@dataclass
class PaymentInfo:
    method: str  # CARD, UPI, etc
    bank_name: Optional[str]
    card_type: Optional[str]  # CREDIT, DEBIT

@dataclass
class DiscountedPrice:
    original_price: Decimal
    final_price: Decimal
    applied_discounts: Dict[str, Decimal]  # discount_name -> amount
    message: str

@dataclass
class CustomerProfile:
    id: str
    tier: str  # e.g., 'gold', 'silver', etc.